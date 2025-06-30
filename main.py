import os
from dotenv import load_dotenv
import argparse
import json
from readmegen.open_ai_client import OpenAiClient

def main():
    parser = argparse.ArgumentParser(description="AI Readme Generator")

    # Authentication
    auth_group = parser.add_argument_group("Authentication")
    auth_group.add_argument("-k", "--api-key", metavar="api_key", type=str,
                            help="OpenAI API key. Can also be stored in .env as OPENAI_API_KEY.")
    # auth_group.add_argument("-t", "--api-token", metavar="api_token", type=str,
    #                         help="OpenAI API token. Can also be stored in .env as OPEN_API_TOKEN.")


    # parser.add_argument("--prompt", type=str)
    parser.add_argument("--directory", type=str,
                        help = "Directory of project to scan."), 

    args = parser.parse_args()

    load_dotenv()
 
    if args.api_key:
        key = args.api_key
    else:
        key = os.environ.get("API_KEY") 

    if not key:
        parser.error("API key and token must be provided either via command line or .env file as API_KEY.")

    client = OpenAiClient(key)

    # if args.prompt:
    #     response = client.prompt(args.prompt)


    if args.directory:
        response = client.generate_readme(args.directory)
        with open(args.directory + "/README.md", "x") as f:
            f.write(response.output_text)

        print(response.output_text)



if __name__ == "__main__":
    main()