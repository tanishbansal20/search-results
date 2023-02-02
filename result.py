def solution(pages, queries, n):
  results = []
  qLength = len(queries)
  pLength = len(pages)
  
  for i in range(qLength):
    memo = {}
    for j in range(pLength):
      common = list(set(queries[i]) & set(pages[j]))
      cal = calculate_weight(pages[j], queries[i], common, n)
      if cal == 0: continue
      if cal in memo: memo[cal].append(j)
      else: memo[cal] = [j]
    results.append(memo)
  arrange_result_formate(results)


def calculate_weight(page, query, common, n):
  cal = 0
  for x in common:
    pos1 = page.index(x)
    pos2 = query.index(x)
    cal += (n - pos1) * (n - pos2)
  return cal


def arrange_result_formate(results):
  result_str = []
  res = ''
  for index in range(len(results)):
    res = 'Q' + str(index+1) + ': '
    data = sorted(results[index], reverse=True)
    count = 0
    for x in data:
      for p in results[index][x]:
        if count == 5: break
        count += 1
        res += 'P' + str(p+1)

    result_str.append(res)
  print_result(result_str)


def print_result(results):
  for result in results:
    print(result)
    