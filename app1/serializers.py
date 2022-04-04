from rest_framework import serializers

from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from urllib import request
from app1.models import User, PersonalUserCard, Qrcode


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name","last_name","username","password","email"]

    def validate_password(self,password):
        return make_password(password)

class PersonalCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalUserCard
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request', None)
        print(request.user)
        personal = PersonalUserCard.objects.create(full_name=validated_data["full_name"],
                                   Designation_or_profession=validated_data['Designation_or_profession'],
                                   city_or_state=validated_data['city_or_state'],
                                   workplace_address=validated_data['workplace_address'],
                                   zip_code=validated_data['zip_code'],
                                   business_location_link=validated_data['business_location_link'],
                                   About_us=validated_data['About_us'],
                                   ContactEmail=validated_data['ContactEmail'],
                                   country=validated_data['country'],
                                   country_code=validated_data['country_code'],
                                   mobile_number=validated_data['mobile_number'],
                                   business_title=validated_data['business_title'],
                                   business_link=validated_data['business_link'],
                                   services=validated_data['services'],
                                   twitter_link=validated_data.get('twitter_link',""),
                                   Instagram_link=validated_data.get('Instagram_link',""),
                                   Linkedin_link=validated_data.get('Linkedin_link',""),
                                   Youtube_channel_link=validated_data.get('Youtube_channel_link',""),
                                   profile_img=validated_data.get('profile_img'),

                                   )

        urs=User.objects.get(username=request.user)
        personal.user=urs
        personal.save()

        return personal


class QrCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qrcode
        fields = ['image','url']

    def create(self, validated_data):
        request = self.context.get('request', None)
        print(request.user)
        qrcode = Qrcode.objects.create(image=validated_data.get("image"),
                                       url=validated_data.get('url',""),
                                       )
        user = User.objects.get(username=request.user)
        qrcode.user = user
        qrcode.save()
        return qrcode


class UserProfileSerilaizer(serializers.ModelSerializer):
    personal_user_card = serializers.SerializerMethodField('get_personal_user_card')
    qr_code = serializers.SerializerMethodField('get_qr_code')

    class Meta:
        model = User
        fields = [
            'mobile_number',
            'personal_user_card',
            'qr_code'
        ]

    @staticmethod
    def get_personal_user_card(obj):
        personal_detail = PersonalUserCard.objects.filter(user_id=obj.id).first()
        if personal_detail:
            return PersonalCardSerializer(personal_detail).data
        return None

    @staticmethod
    def get_qr_code(obj):
        qr_detail = Qrcode.objects.filter(user_id=obj.id).first()
        if qr_detail:
            return QrCodeSerializer(qr_detail).data
        return None







