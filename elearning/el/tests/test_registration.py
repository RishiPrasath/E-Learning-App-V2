from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from el.forms import PortalUserCreationForm
from el.models import PortalUser

class UserRegistrationTest(TestCase):

    def test_valid_user_registration(self):
        # Create a valid user data
        valid_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!',
            'user_type': 'student',
            'photo': SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        }
        form = PortalUserCreationForm(data=valid_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(PortalUser.objects.count(), 1)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.user_type, 'student')
        # Add more assertions here as needed

    def test_email_validations(self):
        # Duplicate email
        PortalUser.objects.create_user(username='user1', email='test@example.com', password='ComplexPass123!')
        form = PortalUserCreationForm(data={
            'username': 'user2',
            'email': 'test@example.com',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!',
            'user_type': 'teacher',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

        # Incorrect email format
        form = PortalUserCreationForm(data={
            'username': 'user3',
            'email': 'invalid_email',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!',
            'user_type': 'teacher',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_user_type_validations(self):
        # Invalid user type
        form = PortalUserCreationForm(data={
            'username': 'user4',
            'email': 'user4@example.com',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!',
            'user_type': 'invalid_type',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('user_type', form.errors)
    

    def test_password_complexity(self):
    # Example: Password lacks uppercase character
        form_data = {
            'username': 'testuser2',
            'email': 'test2@example.com',
            'password1': 'lowercase123!',
            'password2': 'lowercase123!',
            'user_type': 'student',
        }
        form = PortalUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors)  # Assuming your form errors are attached to 'password1'



    def test_photo_upload_valid(self):
        # More realistic image content for JPEG
        valid_photo_content = (b'\xFF\xD8\xFF\xE0' + b'\x00\x10JFIF' + b'\x00\x01' + b'\x01\x01' + b'\x00\x60' + b'\x00\x60' + b'\x00\x00' + b'\xFF\xDB' + b'\x00C' + b'\x00' + b'\x03\x02\x02\x03\x02\x02\x03\x03\x03\x03\x04\x03\x03\x04\x05\x08\x05\x05\x04\x04\x05\n\x07\n\n\n\n\n\x06\x08\x0B\x0C\x0B\n\x0C\t\n\n\n\n')
        valid_photo = SimpleUploadedFile(name='test_image.jpg', content=valid_photo_content, content_type='image/jpeg')
        form_data = {
            'username': 'valid_photo_user',
            'email': 'valid_photo@example.com',
            'password1': 'ValidPassword123!',
            'password2': 'ValidPassword123!',
            'user_type': 'student',
            'photo': valid_photo,
        }
        form = PortalUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors.as_text())

    def test_photo_upload_invalid_type(self):
        # Invalid photo type
        invalid_photo_type = SimpleUploadedFile(name='test_image.svg', content=b'\x00' * 1024, content_type='image/svg+xml')  # SVG file
        form = PortalUserCreationForm(data={
            'username': 'invalid_type_user',
            'email': 'invalid_type@example.com',
            'password1': 'ValidPassword123',
            'password2': 'ValidPassword123',
            'user_type': 'student',
        }, files={'photo': invalid_photo_type})
        self.assertFalse(form.is_valid())
        self.assertIn('photo', form.errors)

    def test_photo_upload_invalid_size(self):
        # Invalid photo size
        invalid_photo_size = SimpleUploadedFile(name='test_image.jpg', content=b'\x00' * (3 * 1024 * 1024), content_type='image/jpeg')  # 3MB JPEG
        form = PortalUserCreationForm(data={
            'username': 'invalid_size_user',
            'email': 'invalid_size@example.com',
            'password1': 'ValidPassword123',
            'password2': 'ValidPassword123',
            'user_type': 'student',
        }, files={'photo': invalid_photo_size})
        self.assertFalse(form.is_valid())
        self.assertIn('photo', form.errors)