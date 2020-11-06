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
        daily_positive = ncov.find_all(class_='inner_value')
        daily_patients = ncov.find_all(class_="txt_ntc")

        daily_list = []
        for value in daily_positive:
            daily_list.append(int(value.string.replace('+', '')))
        for value in daily_patients:
            daily_list.append(int(value.string.replace('+', '')))
        DailyCorona.objects.create(
            date=datetime.date.today(),
            positive=daily_list[0],
            domestic=daily_list[1],
            oversea=daily_list[2],
            cured=daily_list[3],
            quarantined=daily_list[4],
            death=daily_list[5],
            # tests=models.IntegerField(default=0)

        )
        self.stdout.write('complete')
