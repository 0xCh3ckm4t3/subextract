# Subdomain Extractor

A simple Python tool to extract subdomains specifically from waymore output/ list of urls.

## Requirements

- Python 3.x
- `tldextract` package

## Installation

1. Clone this repository
2. Install the required package:
```bash
pip install tldextract
```

## Usage

The tool can be used in two ways:

### 1. Using a file containing URLs

```bash
python subdomain.py -f urls.txt
```

### 2. Passing URLs directly as arguments

```bash
python subdomain.py https://www.example.com https://subdomain.example.com
```

### Options

- `-f, --file`: Input file containing URLs (one per line)
- `-o, --output`: Output file for subdomains (default: subdomains.txt)

## Output

The tool will:
1. Print all found subdomains to the console
2. Save all subdomains to a file (default: subdomains.txt)

## Example

```bash
python subdomain.py -f urls.txt -o my_subdomains.txt
```

This will:
- Read URLs from `urls.txt`
- Extract all subdomains
- Print them to console
- Save them to `my_subdomains.txt`
