from django.shortcuts import render
from django.http import HttpRequest
import csv

def main_page(request):
    context = load_data()
    return render(request,'main_page.html', {'context':context})

def load_data():
    html = "<table>"
    # writing out the header of the html
    html = html + "<thead><tr><th>title1</th><th>title2</th><th>title3</th></tr></thead><tbody>\n"

    with open("data/recipes.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # we replaced this written out line with a loop below
            # html = html + "<td>" + row[0] + "</td><td>" + row[1] + "</td><td>" + row[2] + "</td>
            html = html + "<tr>"
            for data in row:
                html = html + "<td>" + data + "</td>"
            html = html + "</tr>\n"

    html = html + "</tbody></table>"
    return html

