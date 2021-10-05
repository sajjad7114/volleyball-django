from rest_framework import serializers
from .models import Stadium, Match, TransAction, Seat


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

    def save(self):
        match = Match(
            teamA=self.validated_data['teamA'],
            teamB=self.validated_data['teamB'],
            date=self.validated_data['date'],
            stadium=self.validated_data['stadium'],
            available_seats=self.validated_data['available_seats'],
            ticket_price=self.validated_data['ticket_price']
        )
        available_list = match.available_list()
        self.validated_data['available_seats'] = ','.join(list(map(lambda i: str(i), available_list)))

        if self.instance is not None:
            self.instance = self.update(self.instance, self.validated_data)
            assert self.instance is not None, (
                '`update()` did not return an object instance.'
            )
        else:
            self.instance = self.create(self.validated_data)
            assert self.instance is not None, (
                '`create()` did not return an object instance.'
            )
        return self.instance


class TransActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransAction
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'
