# Listing 2.1: ตัวอย่างการใช้ Figma API เพื่อดึงข้อมูล Design
# หัวข้อ: 2.3.2 Figma AI: การออกแบบแบบร่วมมือกับ AI
import requests
import json
from typing import Optional, Dict, Any

class FigmaAPIClient:
    """Client for interacting with Figma API"""
    
    def __init__(self, access_token: str):
        self.base_url = "https://api.figma.com/v1"
        self.headers = {
            "X-Figma-Token": access_token
        }
    
    def get_file(self, file_key: str) -> Optional[Dict[str, Any]]:
        """
        Get file data from Figma
        
        Args:
            file_key: The key of the Figma file
            
        Returns:
            Dictionary containing file data or None if error
        """
        try:
            response = requests.get(
                f"{self.base_url}/files/{file_key}",
                headers=self.headers
            )
            
            if response.status_code == 200:
                file_data = response.json()
                return file_data
            else:
                print(f"Error: {response.status_code}")
                print(f"Message: {response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None
    
    def get_file_nodes(self, file_key: str, node_ids: list) -> Optional[Dict[str, Any]]:
        """
        Get specific nodes from a Figma file
        
        Args:
            file_key: The key of the Figma file
            node_ids: List of node IDs to retrieve
            
        Returns:
            Dictionary containing node data or None if error
        """
        try:
            node_ids_str = ','.join(node_ids)
            response = requests.get(
                f"{self.base_url}/files/{file_key}/nodes",
                headers=self.headers,
                params={"ids": node_ids_str}
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error: {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None
    
    def get_comments(self, file_key: str) -> Optional[list]:
        """
        Get all comments from a Figma file
        
        Args:
            file_key: The key of the Figma file
            
        Returns:
            List of comments or None if error
        """
        try:
            response = requests.get(
                f"{self.base_url}/files/{file_key}/comments",
                headers=self.headers
            )
            
            if response.status_code == 200:
                return response.json().get('comments', [])
            else:
                print(f"Error: {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Replace with your actual Figma access token
    ACCESS_TOKEN = "your_access_token_here"
    FILE_KEY = "your_file_key_here"
    
    # Initialize client
    client = FigmaAPIClient(ACCESS_TOKEN)
    
    # Get file data
    print("Fetching file data...")
    file_data = client.get_file(FILE_KEY)
    
    if file_data:
        print(f"\nFile name: {file_data.get('name')}")
        print(f"Last modified: {file_data.get('lastModified')}")
        print(f"Thumbnail URL: {file_data.get('thumbnailUrl')}")
        print(f"Version: {file_data.get('version')}")
        
        # Print document structure
        document = file_data.get('document', {})
        print(f"\nDocument ID: {document.get('id')}")
        print(f"Document name: {document.get('name')}")
        print(f"Document type: {document.get('type')}")
        
        # Count children (pages)
        children = document.get('children', [])
        print(f"Number of pages: {len(children)}")
        
        for i, page in enumerate(children, 1):
            print(f"  Page {i}: {page.get('name')} (ID: {page.get('id')})")
    
    # Get specific nodes
    print("\n" + "="*50)
    print("Fetching specific nodes...")
    node_ids = ["1:2", "1:3"]  # Replace with actual node IDs
    nodes_data = client.get_file_nodes(FILE_KEY, node_ids)
    
    if nodes_data:
        print(f"Retrieved {len(nodes_data.get('nodes', {}))} nodes")
    
    # Get comments
    print("\n" + "="*50)
    print("Fetching comments...")
    comments = client.get_comments(FILE_KEY)
    
    if comments:
        print(f"Found {len(comments)} comments")
        for comment in comments[:3]:  # Show first 3 comments
            print(f"  - {comment.get('user', {}).get('handle')}: {comment.get('message')[:50]}...")
