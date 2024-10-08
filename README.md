# Youtube Comments Web Scrapper and Summerizer

This repo uses Playwright, Haystack, and Amazon Bedrock to summerize comments on a given youtube video.

## The Web Scrapper
The youtube_comments_scraper.py file lauches a [**Playwright**](https://playwright.dev/python/docs/intro) controlled browser to scrape the comments on a youtube page and save it into a local csv file.

### To run
```
python youtube_comments_scraper.py "<youtube video link>" 
```

## LMM Summerizer Juypter File
haystack.ipynb can then take in the csv file, create a prompt using the values, then pass prompt through a amazon.titan-text-lite-v1 model hosted on AWS Bedrock.

This script uses [**Haystack-ai**](https://haystack.deepset.ai) to set up the csv data processing pipeline and prints out the results off LLM at the end. 

1) change var is code block 3 with the csv file path generated by the scraper.
2) Make sure that have your awssdk credentionals set up on your system. https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html
3) Make sure you have access to `amazon.titan-text-lite-v1` on your aws account through [**Amazon Bedrock**](https://aws.amazon.com/bedrock).
4) Run through all code blocks

## Launch LMM Summerizer as an API

1) Have docker desktop running on your computer
2) docker-compose up --build
3) Run following curl command
```
curl -X 'POST' \
  'http://localhost:1416/haystack_pipeline' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "review_data": {
    "csv_file_path": "comments-2024-08-31 22:51:22.924448.csv"
  },
  "prompt": {},
  "llm": {}
}'
```