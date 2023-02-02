from input import data, pages, queries
from result import solution
class SearchResult:
  def execution():
    contents = data()
    if len(contents) == 0:
      print("Please enter valid data")
      return

    solution(
      pages(contents[0]),
      queries(contents[0]),
      contents[1] + 1
    )

SearchResult.execution()