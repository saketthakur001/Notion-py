# import notion_client
from notion_client import Client, APIResponseError

# credientials.py file if you don't have already, save your key as a variable called key
# import key
from creditionals import key, database_id

# pprint is used to print the output in a more readable format
from pprint import pprint

# This function is used to create a new text block under the parent_id
# def write_text(client, parent_id, text="Hello world!"):
#     """Create a new text block under parent_id and set its content to text."""
#     return client.blocks.children.append(
#         block_id=parent_id,
#         parent=parent_id,
#         children=[
#             {
#                 "object": "block",
#                 "type": "paragraph",
#                 "paragraph": {
#                     "text": [{"type": "text", "text": {"content": text}}] # make sure this is not empty
#                 },
#             }
#         ],
#     )

def write_text(client, parent_id, text="Hello world!"):
    """Create a new text block under parent_id and set its content to text."""
    return client.blocks.children.append(
        block_id=parent_id,
        parent=parent_id,
        children=[
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "text": [{"type": "text", "text": {"content": text}}] # make sure this is not empty
                },
                # add the properties here
                "properties": {
                  "Excerpt": {
                    "rich_text": [
                      {
                        "type": "text",
                        "text": {
                          "content": "hello"
                        }
                      }
                    ]
                  }
                }
            }
        ],
    )

def main():
    # Initialize the client
    client = Client(auth=key)

    # Get the rows of the database
    try:
        rows = client.databases.query(database_id=database_id)
    except APIResponseError as error:
        print(error)
        return

    # Print the rows
    # pprint(rows)

    # Get the first row block
    row_block = rows["results"][0]

    # Get the id of the row block
    row_block_id = row_block["id"]

    # Create a new text block under the row block
    try:
        text = "hey boi"
        print(text) # print the text argument
        write_text(client, row_block_id, text)
    except APIResponseError as error:
        print(error)
        return


if __name__ == "__main__":
    main()