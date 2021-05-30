from rest_framework import serializers

from mainapp.models import Event, Impact


class ImpactSerializer(serializers.ModelSerializer):
    """Иноформация про влияние"""

    class Meta:
        model = Impact
        exclude = ('id', )


class EventSerializer(serializers.ModelSerializer):
    """Инофрмация по событию"""
    impact = ImpactSerializer()

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        impact_data = validated_data.pop('impact')
        impact = Impact.objects.create(**impact_data)
        event = Event.objects.create(impact=impact, **validated_data)
        return event

    def update(self, instance, validated_data):
        impact_data = validated_data.pop('impact')
        impact = instance.impact

        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.finish_date = validated_data.get('finish_date', instance.finish_date)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        impact.priority = impact_data.get('priority', impact.priority)
        impact.affected_services_count = impact_data.get('affected_services_count', impact.affected_services_count)
        impact.save()
        return instance
