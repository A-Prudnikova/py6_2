from demoqa_tests.application_manager import app
from demoqa_tests.page import RegistrationForm
from selene.support.shared import browser


def test_student_registration_form():
    browser.open('automation-practice-form')

    (app.registration_form
     .set_first_name('Anna')
     .set_last_name('Hanna')
     .set_user_email('1@test.ru')
     .set_gender('Female')
     .set_phone_number('1111111111')
     .set_birth_date('20.04.1900')
     .set_subjects('Economics', 'English', 'Arts')
     .set_hobbies('Sports', 'Music')
     .set_picture('1.jpg')
     .set_address('my room')
     .set_state('Haryana')
     .set_city('Panipat')
     .submit_form()
     )

    # Table result
    app.result_registered_user_dialog.table_row(1, value='Anna Hanna')
    app.result_registered_user_dialog.table_row(2, value='1@test.ru')
    app.result_registered_user_dialog.table_row(3, value='Female')
    app.result_registered_user_dialog.table_row(4, value='1111111111')
    app.result_registered_user_dialog.table_row(5, value='20 April,1900')
    app.result_registered_user_dialog.table_row(6, value='Economics, English, Arts')
    app.result_registered_user_dialog.table_row(7, value='Sports, Music')
    app.result_registered_user_dialog.table_row(8, value='1.jpg')
    app.result_registered_user_dialog.table_row(9, value='my room')
    app.result_registered_user_dialog.table_row(10, value='Haryana Panipat')