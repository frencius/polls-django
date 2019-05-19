from django.forms.models import model_to_dict

from polls.models import Question

def get_question():
    try:
        question = Question.objects.all()

        def response_convert(question):
            return dict(
                    id=question.id,
                    question=question.question_text,
                    pub_date=str(question.pub_date)
                )

        result = map(response_convert, list(question))
        
    except Exception:
        raise
    
    return list(result)