from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from cases.models import SumCorona
import requests
import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        # address of data source
        page = requests.get(
            "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=")
        # make object for crawling
        ncov = BeautifulSoup(page.text, 'html.parser')

        # tag, class to pick data from website
        sum_table = ncov.find(class_='num minisize')
        sum_results = sum_table.find_all('td')

        # add data to list
        sum_list = []
        for value in sum_results:
            sum_list.append(int(value.string.replace(' ', '').replace(',', '')))

        # get data from list to db
        SumCorona.objects.create(
            date=datetime.date.today(),
            quarantined=sum_list[0],
            cured=sum_list[1],
            death=sum_list[2],
            positive=sum_list[3],
            negative=sum_list[4],
            pos_neg=sum_list[5],
            in_test=sum_list[6],
            test=sum_list[7]
        )
        self.stdout.write('complete')
