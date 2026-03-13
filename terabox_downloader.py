#!/usr/bin/env python3
"""
TeraBox Downloader CLI
Download files from TeraBox using the Sonzaix API
"""

import requests
import json
import sys
import os
from urllib.parse import quote, unquote
import base64


API_URL = "https://api.sonzaix.indevs.in/terabox"


def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_banner():
    """Print application banner"""
    print("""
╔════════════════════════════════════════╗
║       TeraBox Downloader CLI           ║
║       Powered by Sonzaix API           ║
╚════════════════════════════════════════╝
    """)


def extract_url_from_input(user_input: str) -> str:
    """Extract URL from various input formats"""
    user_input = user_input.strip()
    
    # If input contains &pwd=, extract just the URL part
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


def fetch_download_info(url: str, password: str = "") -> dict:
    """Fetch download information from API"""
    # URL encode the terabox URL
    encoded_url = quote(url, safe='')
    
    # Build the API URL
    api_endpoint = f"{API_URL}?url={encoded_url}"
    if password:
        api_endpoint += f"&pwd={password}"
    
    try:
        response = requests.get(api_endpoint, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": f"Request failed: {str(e)}"}
    except json.JSONDecodeError:
        return {"status": "error", "message": "Invalid JSON response from API"}


def decode_download_link(encoded_url: str) -> str:
    """Decode base64 encoded download URL"""
    try:
        decoded = base64.b64decode(encoded_url).decode('utf-8')
        return decoded
    except Exception:
        return encoded_url


def download_file(url: str, filename: str, size: str) -> bool:
    """Download file with progress indicator"""
    try:
        size_bytes = int(size)
        size_mb = size_bytes / (1024 * 1024)
        
        print(f"\n📥 Downloading: {filename}")
        print(f"   Size: {size_mb:.2f} MB")
        print(f"   URL: {url[:80]}...")
        print()
        
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        downloaded = 0
        total = int(response.headers.get('content-length', 0))
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    
                    if total > 0:
                        percent = (downloaded / total) * 100
                        bar = int(percent / 2) * '█' + int(50 - percent / 2) * '░'
                        print(f"\r   Progress: [{bar}] {percent:.1f}%", end='', flush=True)
        
        print("\n   ✅ Download complete!")
        return True
        
    except Exception as e:
        print(f"\n   ❌ Download failed: {str(e)}")
        return False


def display_file_info(data: dict):
    """Display file information from API response"""
    print("\n" + "=" * 50)
    print("📁 FILE INFORMATION")
    print("=" * 50)
    print(f"  Source       : {data.get('source', 'N/A')}")
    print(f"  Status       : {data.get('status', 'N/A')}")
    print(f"  Total Files  : {data.get('total_files', 0)}")
    print(f"  Is Private   : {data.get('is_private', False)}")
    print("=" * 50)


def display_files_list(files: list):
    """Display list of files"""
    print("\n📋 AVAILABLE FILES:")
    print("-" * 50)
    
    for idx, file in enumerate(files, 1):
        filename = file.get('filename', 'Unknown')
        size = int(file.get('size', 0))
        size_mb = size / (1024 * 1024)
        
        print(f"  [{idx}] {filename}")
        print(f"      Size: {size_mb:.2f} MB")
        if file.get('thumbnail'):
            print(f"      Thumbnail: {file['thumbnail']}")
        print()


def main_menu():
    """Main menu loop"""
    while True:
        print_banner()
        print("  Main Menu")
        print("  " + "-" * 40)
        print("  1. Download from TeraBox URL")
        print("  2. Exit")
        print("  " + "-" * 40)
        
        choice = input("\n  Select option (1-2): ").strip()
        
        if choice == '1':
            download_workflow()
        elif choice == '2':
            print("\n  👋 Goodbye!\n")
            sys.exit(0)
        else:
            print("\n  ❌ Invalid option. Please try again.\n")
            input("  Press Enter to continue...")
            clear_screen()


def download_workflow():
    """Download workflow"""
    clear_screen()
    print_banner()
    print("  Download from TeraBox")
    print("  " + "-" * 40)
    
    # Get URL from user
    print("\n  Enter TeraBox URL (with optional &pwd=xxx):")
    print("  Example: https://www.terabox.app/indonesian/sharing/init?surl=xxx&pwd=xxx")
    print()
    
    user_input = input("  > ").strip()
    
    if not user_input:
        print("\n  ❌ URL cannot be empty!")
        input("  Press Enter to continue...")
        return
    
    # Extract URL and password
    terabox_url = extract_url_from_input(user_input)
    password = extract_password_from_input(user_input)
    
    # If no password in URL, ask for it
    if not password:
        print("\n  This link might be password protected.")
        print("  Leave empty if no password required.")
        password = input("  Enter password (or press Enter to skip): ").strip()
    
    # Fetch download info
    print("\n  ⏳ Fetching download information...")
    data = fetch_download_info(terabox_url, password)
    
    # Check response status
    if data.get('status') != 'success':
        print(f"\n  ❌ Error: {data.get('message', 'Unknown error')}")
        print(f"  Debug: {data.get('debug', [])}")
        input("  Press Enter to continue...")
        return
    
    # Display file info
    display_file_info(data)
    files = data.get('files', [])
    
    if not files:
        print("\n  ❌ No files found!")
        input("  Press Enter to continue...")
        return
    
    display_files_list(files)
    
    # Select file to download
    if len(files) == 1:
        selected_idx = 0
    else:
        try:
            sel = input(f"  Select file to download (1-{len(files)}) or 'a' for all: ").strip()
            if sel.lower() == 'a':
                # Download all files
                for idx, file in enumerate(files):
                    process_download(file, idx + 1, len(files))
                input("\n  Press Enter to continue...")
                return
            selected_idx = int(sel) - 1
            if selected_idx < 0 or selected_idx >= len(files):
                print("\n  ❌ Invalid selection!")
                input("  Press Enter to continue...")
                return
        except ValueError:
            print("\n  ❌ Invalid selection!")
            input("  Press Enter to continue...")
            return
    
    # Process download
    file = files[selected_idx]
    process_download(file, selected_idx + 1, len(files))
    
    input("\n  Press Enter to continue...")


def process_download(file: dict, current: int, total: int):
    """Process single file download"""
    filename = file.get('filename', 'download')
    size = file.get('size', '0')
    
    # Get download link (may be base64 encoded)
    download_link = file.get('download_link', '')
    
    # Try to decode if it's base64
    if download_link.startswith('aHR0cHM') or download_link.startswith('http'):
        actual_url = decode_download_link(download_link)
    else:
        actual_url = download_link
    
    # If we have multiple files, show progress
    if total > 1:
        print(f"\n  File {current}/{total}")
    
    # Download the file
    download_file(actual_url, filename, size)


if __name__ == "__main__":
    try:
        clear_screen()
        main_menu()
    except KeyboardInterrupt:
        print("\n\n  ⚠️  Interrupted by user")
        sys.exit(0)
