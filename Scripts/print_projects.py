#!/usr/bin/env python3
"""
Print Projects Summary

Reads projects.json and outputs a formatted summary of all projects.
Useful for quick reference or generating text for other purposes.

Usage:
    python scripts/print_projects.py
    python scripts/print_projects.py --format table
    python scripts/print_projects.py --format list
"""

import json
import sys
from pathlib import Path


def load_projects():
    """Load projects from projects.json."""
    script_dir = Path(__file__).parent
    json_path = script_dir.parent / "projects.json"
    
    if not json_path.exists():
        print(f"Error: projects.json not found at {json_path}")
        sys.exit(1)
    
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def format_status(status: str) -> str:
    """Convert status code to human-readable string."""
    status_map = {
        "production": "✅ Production",
        "active_development": "🔄 Active Development",
        "prototype": "🧪 Prototype",
        "maintenance": "🔧 Maintenance",
        "archived": "📦 Archived"
    }
    return status_map.get(status, status)


def print_header(data: dict):
    """Print portfolio header."""
    portfolio = data.get("portfolio", {})
    print("=" * 60)
    print(f"  {portfolio.get('name', 'Projects Portfolio')}")
    print(f"  Maintainer: {portfolio.get('maintainer', 'Unknown')}")
    print(f"  Last Updated: {portfolio.get('last_updated', 'Unknown')}")
    print("=" * 60)
    print()


def print_list_format(projects: list):
    """Print projects in list format."""
    for i, project in enumerate(projects, 1):
        print(f"{i}. {project['name']}")
        print(f"   {project['tagline']}")
        print(f"   Status: {format_status(project['status'])}")
        print(f"   Tech: {', '.join(project['tech_stack'][:4])}")
        if len(project['tech_stack']) > 4:
            print(f"         + {len(project['tech_stack']) - 4} more")
        print()


def print_table_format(projects: list):
    """Print projects in table format."""
    # Calculate column widths
    name_width = max(len(p['name']) for p in projects) + 2
    status_width = 20
    
    # Header
    print(f"{'Project':<{name_width}} {'Status':<{status_width}} Tech Stack")
    print("-" * (name_width + status_width + 30))
    
    # Rows
    for project in projects:
        tech_str = ", ".join(project['tech_stack'][:3])
        if len(project['tech_stack']) > 3:
            tech_str += f" +{len(project['tech_stack']) - 3}"
        
        status = format_status(project['status'])
        print(f"{project['name']:<{name_width}} {status:<{status_width}} {tech_str}")


def print_detailed(projects: list):
    """Print detailed project information."""
    for project in projects:
        print("-" * 60)
        print(f"📁 {project['name']}")
        print(f"   {project['full_name']}")
        print()
        print(f"   {project['description']}")
        print()
        print(f"   Status: {format_status(project['status'])}")
        print(f"   Folder: {project['folder']}")
        print()
        print("   Tech Stack:")
        for tech in project['tech_stack']:
            print(f"     • {tech}")
        print()
        print("   Highlights:")
        for highlight in project.get('highlights', []):
            print(f"     ★ {highlight}")
        print()


def main():
    # Parse simple args
    format_type = "detailed"
    if len(sys.argv) > 1:
        if sys.argv[1] in ["--format", "-f"] and len(sys.argv) > 2:
            format_type = sys.argv[2]
        elif sys.argv[1] == "--help":
            print(__doc__)
            sys.exit(0)
    
    # Load data
    data = load_projects()
    projects = data.get("projects", [])
    
    if not projects:
        print("No projects found.")
        sys.exit(0)
    
    # Print header
    print_header(data)
    
    # Print based on format
    if format_type == "list":
        print_list_format(projects)
    elif format_type == "table":
        print_table_format(projects)
    else:
        print_detailed(projects)
    
    # Footer
    print("-" * 60)
    print(f"Total: {len(projects)} projects")


if __name__ == "__main__":
    main()

