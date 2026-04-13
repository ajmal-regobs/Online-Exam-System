from pydantic import BaseModel, field_validator


class QuestionCreate(BaseModel):
    question_text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_option: str

    @field_validator("correct_option")
    @classmethod
    def validate_correct_option(cls, v: str) -> str:
        if v.lower() not in ("a", "b", "c", "d"):
            raise ValueError("correct_option must be one of: a, b, c, d")
        return v.lower()


class QuestionResponse(BaseModel):
    id: int
    question_text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_option: str

    model_config = {"from_attributes": True}
