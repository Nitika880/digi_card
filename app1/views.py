from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from app1.models import User, PersonalUserCard, Qrcode
from app1.serializers import UserSerializer, PersonalCardSerializer, QrCodeSerializer, UserProfileSerilaizer


class RegisterView(CreateAPIView):
    permission_classes = [AllowAny,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={"message": "User created successfully.",
                                  "first_name": serializer.data["first_name"],
                                  "last_name": serializer.data["last_name"],
                                  "username": serializer.data["username"],
                                  "email": serializer.data["email"],

                                 }, status=status.HTTP_201_CREATED)
        return Response(data={"message": "Password or username policy failed."}, status=status.HTTP_400_BAD_REQUEST)



class PersonalCardView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PersonalCardSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class QRCodeAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    # queryset = Qrcode.objects.all()
    serializer_class = QrCodeSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class GetUserProfileView(RetrieveAPIView):
    lookup_field = "user_key"
    permission_classes = [AllowAny, ]
    # queryset = Qrcode.objects.all()
    # serializer_class = PersonalCardSerializer

    def get(self, request, *args, **kwargs):
        user_key = kwargs.get(self.lookup_field)
        if not user_key:
            return Response(
                data={
                    'error': "pass user key"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        user = User.objects.filter(user_key=user_key).first()
        print("user:", user)
        if not user:
            return Response(
                data={
                    'error': "user does not exist"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        user_profile = UserProfileSerilaizer(user).data

        return Response(
            data=user_profile,
            status=status.HTTP_400_BAD_REQUEST
        )

        # personal_details = PersonalUserCard.objects.filter(user_id=user).first()
        # if personal_details:
        #     return Response(data={
        #         "first_name": request.user.full_name,
        #         "last_name" : request.user.Designation_or_profession,
        #         "city_or_state": request.user.city_or_state,
        #         "workplace_address":request.user.workplace_address,
        #         "zip_code": request.user.zip_code,
        #         "business_location_link": request.user.business_location_link,
        #         "About_us": request.user.About_us,
        #         "ContactEmail":request.user.ContactEmail,
        #         "country": request.user.country,
        #         "country_code": request.user.country_code,
        #         "mobile_number":request.user.mobile_number,
        #         "business_title":request.user.business_title,
        #         "business_link" : request.user.business_link,
        #         "services": request.user.services,
        #         "facebook_link":request.user.facebook_link,
        #         "twitter_link":request.user.twitter_link,
        #         "Instagram_link":request.user.Instagram_link,
        #         "Linkedin_link":request.user.Linkedin_link,
        #         "Youtube_channel_link":request.user.Youtube_channel_link,
        #         "profile_img":request.user.profile_img
        #
        #
        #
        #
        #
        #
        #
        #     })
        #
        #
        #
        #
        # return self.retrieve(request, *args, **kwargs)




# def fetch_data(request,user_key= None):
#     if not user_key:
#         return HttpResponse("pass user key")
#     else:
#         print("user_key:", user_key)
#         user = User.objects.filter(user_key=user_key).first()
#         print("user:", user)
#         if not user:
#             return HttpResponse("user doesnt exist")
#     personal_details = PersonalUserCard.objects.filter(user_id=user).first()
#     print(personal_details)
#     qr_details = Qrcode.objects.filter(user_id=user).first()
#     print(qr_details)
#     return HttpResponse("done")


