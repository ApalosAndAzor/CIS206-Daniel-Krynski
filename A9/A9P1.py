import re

p1x1 = "ABCDEFabcdef123450"
p1x2 = "*&%@#!}{"
p1y1 = re.match('^[a-zA-Z0-9]+$', p1x1)
p1y2 = re.match('^[a-zA-Z0-9]+$', p1x2)
print(p1y1)
print(p1y2)

p2x1 = "ab"
p2x2 = "abc"
p2x3 = "a"
p2x4 = "ab"
p2x5 = "abb"
p2y1 = re.match('ab*', p2x1)
p2y2 = re.match('ab*', p2x2)
p2y3 = re.match('ab*', p2x3)
p2y4 = re.match('ab*', p2x4)
p2y5 = re.match('ab*', p2x5)
print(p2y1)
print(p2y2)
print(p2y3)
print(p2y4)
print(p2y5)

p3x1 = "ab"
p3x2 = "abc"
p3x3 = "a"
p3x4 = "ab"
p3x5 = "abb"
p3y1 = re.match('ab+', p3x1)
p3y2 = re.match('ab+', p3x2)
p3y3 = re.match('ab+', p3x3)
p3y4 = re.match('ab+', p3x4)
p3y5 = re.match('ab+', p3x5)
print(p3y1)
print(p3y2)
print(p3y3)
print(p3y4)
print(p3y5)

p4x1 = "aab_cbbbc"
p4x2 = "aab_Abbbc"
p4x3 = "Aaab_abbbc"
p4y1 = re.match('[a-z]+_[a-z]+', p4x1)
p4y2 = re.match('[a-z]+_[a-z]+', p4x2)
p4y3 = re.match('[a-z]+_[a-z]+', p4x3)
print(p4y1)
print(p4y2)
print(p4y3)

p5x1 = "The quick brown fox jumps over the lazy dog."
p5x2 = " The quick brown fox jumps over the lazy dog."
p5y1 = re.match(r'^\w+', p5x1)
p5y2 = re.match(r'^\w+', p5x2)
print(p5y1)
print(p5y2)

p6x1 = "The quick brown fox jumps over the lazy dog."
p6x2 = "Python Exercises."
p6y1 = re.search(r'\b\w*z\w*\b', p6x1)
p6y2 = re.search(r'\b\w*z\w*\b', p6x2)
print(p6y1)
print(p6y2)

p7x1 = "216.08.094.196"
p7y1 = re.sub(r'\b0+(\d)', r'\1', p7x1)
print(p7y1)

p8x1 = "The quick brown fox jumps over the lazy dog."
p8y1 = re.search('fox', p8x1)
p8y2 = re.search('dog', p8x1)
p8y3 = re.search('horse', p8x1)
print(p8y1)
print(p8y2)
print(p8y3)

p9x1 = "The quick brown fox jumps over the lazy dog."
p9y1 = re.search('fox', p9x1)
print(p9y1)
print(f"Found 'fox' at index {p9y1.start()} in the string: '{p9x1}'")

p10x1 = "Replace expressions"
p10x2 = "Code_Examples"
p10y1 = re.sub(r'\s', '_', p10x1)
p10y2 = re.sub(r'_', ' ', p10x2)
print(p10y1)
print(p10y2)

url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author"
date_pattern = r'/(\d{4})/(\d{1,2})/(\d{1,2})/'
date_match = re.search(date_pattern, url)

if date_match:
  url_year = date_match.group(1)
  url_month = date_match.group(2)
  url_day = date_match.group(3)
  print(f"Year: {url_year}, Month: {url_month}, Day: {url_day}")
else:
  print("No date pattern found in the URL.")

p12x1 = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
p12y1 = re.findall(r'\b[ae]\w+', p12x1)
print(p12y1)

p13x1 = "Python Exercises, PHP exercises."
p13y1 = re.sub(r'[\s,.]', ":", p13x1)
print(p13y1)

p14x1 = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
p14y1 = re.findall(r'\b[ae]\w+', p14x1)
print(p14y1)

p15x1 = "Python      Exercises"
p15y1 = re.sub(r'\s+', ' ', p15x1)
print(p15y1)