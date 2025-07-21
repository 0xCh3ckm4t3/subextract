import tldextract
from urllib.parse import urlparse
import argparse
import sys

def extract_subdomains(urls):
    """Extract unique subdomains from a list of URLs."""
    subdomains = set()
    
    for url in urls:
        # Ensure URL has a scheme (http:// or https://) for urlparse
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        try:
            # Parse the URL
            parsed_url = urlparse(url)
            # Extract domain components
            extracted = tldextract.extract(parsed_url.netloc)
            # Get subdomain (if it exists)
            if extracted.subdomain:
                subdomain = f"{extracted.subdomain}.{extracted.domain}.{extracted.suffix}"
                subdomains.add(subdomain)
            # Also add the main domain if it has a subdomain like 'www'
            if extracted.domain and extracted.suffix:
                if extracted.subdomain == 'www':
                    base_domain = f"{extracted.domain}.{extracted.suffix}"
                    subdomains.add(f"www.{base_domain}")
        except Exception as e:
            print(f"Error processing URL {url}: {e}", file=sys.stderr)
    
    return sorted(subdomains)

def read_urls_from_file(file_path):
    """Read URLs from a file, one per line."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}", file=sys.stderr)
        sys.exit(1)

def write_subdomains_to_file(subdomains, output_file):
    """Write subdomains to an output file."""
    try:
        with open(output_file, 'w') as file:
            for subdomain in subdomains:
                file.write(subdomain + '\n')
        print(f"Subdomains written to {output_file}")
    except Exception as e:
        print(f"Error writing to file {output_file}: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Extract subdomains from a list of URLs.")
    parser.add_argument('-f', '--file', help="Input file containing URLs (one per line)")
    parser.add_argument('-o', '--output', default='subdomains.txt', help="Output file for subdomains (default: subdomains.txt)")
    parser.add_argument('urls', nargs='*', help="List of URLs to process (optional if -f is used)")
    
    args = parser.parse_args()
    
    # Get URLs from file or command-line arguments
    if args.file:
        urls = read_urls_from_file(args.file)
    elif args.urls:
        urls = args.urls
    else:
        print("Error: Please provide URLs via -f/--file or as command-line arguments.", file=sys.stderr)
        parser.print_help()
        sys.exit(1)
    
    # Extract subdomains
    subdomains = extract_subdomains(urls)
    
    # Print results
    if subdomains:
        print("\nExtracted Subdomains:")
        for subdomain in subdomains:
            print(subdomain)
    else:
        print("No subdomains found.")
    
    # Write to output file
    if subdomains:
        write_subdomains_to_file(subdomains, args.output)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(1)