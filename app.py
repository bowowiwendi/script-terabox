#!/usr/bin/env python3
"""
TeraBox Downloader - Web Version
Flask-based web interface for downloading files from TeraBox
"""

from flask import Flask, render_template, request, jsonify, send_file, Response
import requests
import json
import os
import base64
from urllib.parse import quote
import io
import re


app = Flask(__name__)

API_URL = "https://api.sonzaix.indevs.in/terabox"


def extract_url_from_input(user_input: str) -> str:
    """Extract URL from various input formats"""
    user_input = user_input.strip()
    
    if '&pwd=' in user_input:
        url_part = user_input.split('&pwd=')[0]
        return url_part.strip()
    
    return user_input


def extract_password_from_input(user_input: str) -> str:
    """Extract password from input if present"""
    user_input = user_input.strip()
    
    if '&pwd=' in user_input:
        parts = user_input.split('&pwd=')
        if len(parts) > 1:
            return parts[1].strip()
    
    return ""


def decode_download_link(encoded_url: str) -> str:
    """Decode base64 encoded download URL"""
    try:
        decoded = base64.b64decode(encoded_url).decode('utf-8')
        return decoded
    except Exception:
        return encoded_url


def sanitize_filename(filename: str) -> str:
    """Sanitize filename for safe download"""
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    return filename


@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@app.route('/api/fetch', methods=['POST'])
def fetch_info():
    """Fetch file information from TeraBox"""
    data = request.get_json()
    
    if not data or 'url' not in data:
        return jsonify({'status': 'error', 'message': 'URL is required'}), 400
    
    url = data['url'].strip()
    password = data.get('password', '').strip()
    
    if not url:
        return jsonify({'status': 'error', 'message': 'URL cannot be empty'}), 400
    
    # Extract URL and password
    terabox_url = extract_url_from_input(url)
    terabox_pwd = extract_password_from_input(url) or password
    
    # Fetch from API
    encoded_url = quote(terabox_url, safe='')
    api_endpoint = f"{API_URL}?url={encoded_url}"
    if terabox_pwd:
        api_endpoint += f"&pwd={terabox_pwd}"
    
    try:
        response = requests.get(api_endpoint, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        if result.get('status') == 'success':
            # Decode download links for frontend
            for file in result.get('files', []):
                if 'download_link' in file:
                    file['decoded_link'] = decode_download_link(file['download_link'])
        
        return jsonify(result)
        
    except requests.exceptions.RequestException as e:
        return jsonify({'status': 'error', 'message': f'Request failed: {str(e)}'}), 500
    except json.JSONDecodeError:
        return jsonify({'status': 'error', 'message': 'Invalid JSON response'}), 500


@app.route('/api/download', methods=['POST'])
def download():
    """Stream download file"""
    data = request.get_json()
    
    if not data or 'url' not in data:
        return jsonify({'status': 'error', 'message': 'Download URL is required'}), 400
    
    download_url = data['url']
    filename = data.get('filename', 'download')
    
    filename = sanitize_filename(filename)
    
    try:
        response = requests.get(download_url, stream=True, timeout=60)
        response.raise_for_status()
        
        content_type = response.headers.get('content-type', 'application/octet-stream')
        content_length = response.headers.get('content-length', '')
        
        def generate():
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    yield chunk
        
        return Response(
            generate(),
            mimetype=content_type,
            headers={
                'Content-Disposition': f'attachment; filename="{filename}"',
                'Content-Length': content_length
            }
        )
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Download failed: {str(e)}'}), 500


@app.route('/api/proxy-download')
def proxy_download():
    """Proxy download endpoint for direct streaming"""
    url = request.args.get('url', '')
    filename = request.args.get('filename', 'download')
    
    if not url:
        return jsonify({'status': 'error', 'message': 'URL is required'}), 400
    
    try:
        response = requests.get(url, stream=True, timeout=60)
        response.raise_for_status()
        
        return Response(
            response.iter_content(chunk_size=8192),
            mimetype=response.headers.get('content-type', 'application/octet-stream'),
            headers={
                'Content-Disposition': f'attachment; filename="{sanitize_filename(filename)}"'
            }
        )
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
