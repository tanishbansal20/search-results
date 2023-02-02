def data():
  print("Press 1: if you want to enter data manually")
  print("Press 2: if you want to use sameple input data")

  choice = input()
  contents = []

  match choice:
    case '1':
      print("Enter/Paste your content. Ctrl-D or Ctrl-Z to save it.")
      while True:
        try:
          line = input()
          if line.find('P ') != 0 or line.find('Q ') != 0:
            print("Invalid data: Data will start with P or Q")
            return []
        except EOFError:
          break
        contents.append(line)
    case '2':
      lines = open("sample_input_data.txt", "r")
      contents = lines.read().split('\n')
      return [contents, 8]
    case other:
      print("Invalid input")
      return []

  print("Enter maximum keywords:")
  try:
    n = int(input())
  except ValueError:
    print("you need to enter only interger")
    return []

  return [contents, n]
  

def pages(contents, page_memo = []):
    for content in contents:
      if content[0] == 'P':
        page_memo.append(content.split(' '))

    return page_memo


def queries(contents, query = []):
  for content in contents:
    if content[0] == 'Q':
      query.append(content.split(' '))

  return query