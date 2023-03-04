from django.contrib.auth.models import User, Group
from bar.models import ItemCard, Order, Extras
from rest_framework import serializers
from datetime import date, datetime


"""class CheckListSerializer(serializers.ModelSerializer):


    def get_report_status(self, checklist):

        request = self.context['request']

        date = request.query_params.get('date')
        datetime_date = datetime.strptime(date, "%d.%m.%Y").date()

        report = Report.objects.filter(checklist_id=checklist.id).filter(date=datetime_date)

        if report.exists():

            return "True"
        else:
            return "False"

    class Meta:
        model = CheckList
        fields = [f.name for f in CheckList._meta.fields] + ['report_status']"""


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemCard
        fields = '__all__'



