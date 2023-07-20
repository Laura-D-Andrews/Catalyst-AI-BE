from rest_framework import serializers
from .models import User, Write, VisualArt, Movement, Music, Note, Welcome, Definition


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username'
        ]


class WriteInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Write
        fields = [
            'id',
            'user',
            'style',
            'theme',
            'category',
            'sentiment',
            'emotion',
            'prompt_length',
            'input_length',
        ]


class WriteOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Write
        fields = [
            'id',
            'user',
            'style',
            'theme',
            'category',
            'sentiment',
            'emotion',
            'prompt_length',
            'input_length',
            'created_at',
            'output',
        ]


class VisualArtInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisualArt
        fields = [
            'id',
            'user',
            'medium',
            'theme',
            'sentiment',
            'emotion',
            'prompt_length',
            'input_length',
        ]


class VisualArtOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisualArt
        fields = [
            'id',
            'user',
            'medium',
            'theme',
            'sentiment',
            'emotion',
            'prompt_length',
            'created_at',
            'output',
        ]


class MovementInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = [
            'id',
            'user',
            'theme',
            'somatic',
            'sentiment',
            'emotion',
            'prompt_length',
            'input_length',
        ]


class MovementOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = [
            'id',
            'user',
            'theme',
            'somatic',
            'sentiment',
            'emotion',
            'prompt_length',
            'input_length',
            'created_at',
            'output',
        ]


class MusicInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = [
            'id',
            'user',
            'exploration',
            'concept',
            'element',
            'emotion',
            'prompt_length',
            'input_length'
        ]


class MusicOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = [
            'id',
            'user',
            'exploration',
            'concept',
            'element',
            'emotion',
            'prompt_length',
            'input_length',
            'created_at',
            'output',
        ]


class AllPromptsArchiveSerializer(serializers.ModelSerializer):
    music = MusicOutputSerializer(many=True, read_only=True)
    visual_arts = VisualArtOutputSerializer(many=True, read_only=True)
    movements = MovementOutputSerializer(many=True, read_only=True)
    writes = WriteOutputSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'music',
            'visual_arts',
            'movements',
            'writes'
        ]


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = [
            'text',
            'write',
            'visual_art',
            'movement',
            'music',
        ]


class WelcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Welcome
        fields = [
            'id',
            'output_text',
        ]


class DefinitionInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definition
        fields = [
            'id',
            'word',
        ]


class DefinitionOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definition
        fields = [
            'id',
            'word',
            'definition'
        ]
