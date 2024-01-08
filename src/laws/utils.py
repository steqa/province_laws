from django.core import serializers

def form_response(chapter_model, text_model):
    response = []
    for chapter in chapter_model:
        response.append({
            'chapter': serializers.serialize('json', [chapter]),
            'offences': serializers.serialize('json', text_model.filter(chapter=chapter))
        })

    return response