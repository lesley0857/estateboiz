from rest_framework.serializers import ModelSerializer,EmailField,CharField
from django.contrib.auth import get_user_model
from England.models import Groupss, Chatmessage

class Group_serializer(ModelSerializer):
    class Meta:
        model = Groupss
        fields = ['id','name','grouphead','users']

class  Chatmessage_serializer(ModelSerializer):
    class Meta:
        model =  Chatmessage
        fields = ['id','chat']

User = get_user_model()

# creating a user from an API request restframework already checks if a user exists
class user_creation_serializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username','email','password']
        extra_kwargs = {'password':{'write_only':True} } 
        

    def create(self,validated_data):
        print('jdfif',validated_data)
        username = validated_data['username']
        password = validated_data['password']
        user_obj = User(username=username,password=password)#,is_super_user,is_staff=True)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

class user_login_serializer(ModelSerializer):
    token = CharField(allow_blank=True,read_only=True)
    class Meta:
        model = User
        fields = ['username','password','token']
        extra_kwargs = {'password': {'write_only': True}} 
    
    def validate(self, data):
        
        return data
