from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from cases.models import DailyCorona
import requests
import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        page = requests.get(
            "https://ncov.kdca.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=")
        ncov = BeautifulSoup(page.text, 'html.parser')

        # find values by html class
        daily_cases = ncov.find_all(class_='ca_value')
        oversea_daily = ncov.find(class_='sumline')

        DailyCorona.objects.create(
            date=datetime.date.today(),
            positive=int(daily_cases[6].string.replace(',', '')),

            # subtract the oversea cases from daily cases in ca_value
            domestic=daily_list[1],
            oversea=daily_list[2],

            #
            cured=daily_list[3],
            quarantined=daily_list[4],

            death=daily_list[5],

        )
        self.stdout.write('complete')
