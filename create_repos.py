name: Run Python Script

on:
  push:
    branches:
      - main  # Chạy workflow khi có thay đổi trên nhánh main

jobs:
  run-script:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'  # Chọn phiên bản Python phù hợp

      - name: Install dependencies
        run: pip install requests

      - name: Run script
        run: python create_repos.py
        env:
          GITHUB_USERNAME: ${{ secrets.GITHUB_USERNAME }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
