from notion_client import Client

notion = Client(auth=key)
database_id = database_id

def add_item(text):
  try:
    response = notion.pages.create(
      parent={"database_id": database_id},
      properties={
        "title": {
          "title": [
            {
              "text": {
                "content": text
              }
            }
          ]
        }
      },
    )
    print(response)
    print("Success! Entry added.")
  except Exception as error:
    print(error)

def add_property(name, type, options):
  try:
    response = notion.databases.update(
      database_id=database_id,
      properties={
        name: {
          "type": type,
          "multi_select": {
            "options": options
          }
        }
      },
    )
    print(response)
    print("Success! Property added.")
  except Exception as error:
    print(error)

# # Example usage
add_property("genre", "multi_select", [{"name": "Fantasy", "color": "pink"}, {"name": "Sci-Fi", "color": "blue"}, {"name": "Horror", "color": "red"}])
