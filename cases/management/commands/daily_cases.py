from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from cases.models import DailyCorona
import requests
import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        page = requests.get(
            "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=")
        ncov = BeautifulSoup(page.text, 'html.parser')

        # find values by html class
        daily_positive = ncov.find_all(class_='inner_value')
        daily_patients = ncov.find_all(class_="txt_ntc")

        # list used for scrapped data add to db
        daily_list = []

        # make values fit for db datatype : string to integer
        for value in daily_positive:
            daily_list.append(int(value.string.replace(' ', '').replace(',', '')))
        for value in daily_patients:
            daily_list.append(int(value.string.replace(' ', '').replace(',', '')))

        DailyCorona.objects.create(
            date=datetime.date.today(),
            positive=daily_list[0],
            domestic=daily_list[1],
            oversea=daily_list[2],
            cured=daily_list[3],
            quarantined=daily_list[4],
            death=daily_list[5],

        )
        self.stdout.write('complete')
