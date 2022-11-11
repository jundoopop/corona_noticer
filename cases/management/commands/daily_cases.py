from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from cases.models import DailyCasesNew
import requests
import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        page = requests.get(
            "https://ncov.kdca.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=")
        ncov = BeautifulSoup(page.text, 'html.parser')

        # find values by html class
        daily_cases = ncov.find_all(class_='ca_value')
        daily_positives = int(daily_cases[6].string.replace(',', ''))
        oversea_daily = int(ncov.find(class_='sumline').td.text)

        DailyCasesNew.objects.create(
            date=datetime.date.today(),
            positive=daily_positives,
            # subtract the oversea cases from daily cases in ca_value
            domestic=daily_positives - oversea_daily,
            oversea=oversea_daily,

            # no cured data since 2021, because of covid policy has changed
            quarantined=int(daily_cases[2].text),

            death=int(daily_cases[0].text),

        )
        self.stdout.write('complete')
