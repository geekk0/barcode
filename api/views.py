from bar.models import ItemCard, Order, Extras
from rest_framework import viewsets
from rest_framework import permissions
from api.serializer import MenuSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from datetime import date, datetime
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.views.decorators.csrf import csrf_exempt


"""class Authorization(viewsets.ModelViewSet):

    def get_queryset(self):

        username = self.request.query_params.get('username')
        user = User.objects.get(username=username)

        user_profile = UserProfile.objects.filter(user=user)

        return user_profile

    def get_serializer_class(self):
        serializer_class = UserProfileSerializer
        return serializer_class

    def get_permissions(self):
        permission_classes = [permissions.IsAuthenticated()]
        return permission_classes


class GetCheckList(viewsets.ModelViewSet):

    def get_queryset(self):
        date = self.request.query_params.get('date')
        datetime_date = datetime.strptime(date, "%d.%m.%Y").date()
        user = self.request.user
        user_groups = Group.objects.filter(user=user)
        all_checklists = CheckList.objects.all()
        user_checklists = all_checklists.filter(executants=user) | all_checklists.filter(execs_groups__in=user_groups)
        result_user_checklists_list_ids = []

        for checklist in user_checklists:

            if checklist.check_date(datetime_date) is True:
                # print(checklist.name)
                result_user_checklists_list_ids.append(checklist.id)

        result_user_checklists = CheckList.objects.filter(id__in=result_user_checklists_list_ids)

        return result_user_checklists

    def get_serializer_class(self):
        serializer_class = CheckListSerializer
        return serializer_class

    def get_permissions(self):
        permission_classes = [permissions.IsAuthenticated()]
        return permission_classes"""






class GetMenu(viewsets.ModelViewSet):

    def get_queryset(self):
        menu_queryset = ItemCard.objects.filter(available=True)

        return menu_queryset

    def get_serializer_class(self):
        serializer_class = MenuSerializer
        return serializer_class

    """def get_permissions(self):
        permission_classes = [permissions.IsAuthenticated()]
        return permission_classes"""











"""class DateConverter:
    regex = r"\d{1,2}-\d{1,2}-\d{4}"
    format = "%d-%m-%Y"

    def to_python(self, value: str) -> date:
        return datetime.strptime(value, self.format).date()

    def to_url(self, value: date) -> str:
        return value.strftime(self.format)


class GetCheckListSteps(viewsets.ModelViewSet):

    def get_queryset(self):
        checklist_id = self.request.query_params.get('checklist_id')

        checklist = CheckList.objects.get(id=checklist_id)

        steps = Step.objects.filter(checklist=checklist).order_by("number")

        return steps

    def get_serializer_class(self):
        serializer_class = StepsSerializer
        return serializer_class

    def get_permissions(self):
        permission_classes = [permissions.IsAuthenticated()]
        return permission_classes


class StoreReportStep(viewsets.ModelViewSet):

    def get_queryset(self):

        checklists = CheckList.objects.all()

        return checklists

    def get_serializer_class(self):
        serializer_class = ReportStepSerializer
        return serializer_class

    def get_permissions(self):
        permission_classes = [permissions.IsAuthenticated()]
        return permission_classes

    @action(detail=True, methods=['post'])
    def upload_step(self, request):
        try:
            file = request.data['file']
        except KeyError:
            raise ParseError('Request has no resource file attached')
        print(request.data)


class CreateReportStep(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, JSONParser, FormParser]
    # @permission_classes([IsAuthenticated])

    def post(self, request, format=None):

        serializer = ReportStepSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateReport(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""