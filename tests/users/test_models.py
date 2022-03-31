import pytest


def test_user_str(base_user):
    """Test the user model string representation"""
    assert base_user.__str__() == f'{base_user.username}'


def test_user_full_name(base_user):
    """Test that the user models get_full_name method works"""
    full_name = f'{base_user.first_name} {base_user.second_name}'
    assert base_user.get_full_name == full_name


def test_user_short_name(base_user):
    """Test that the user models get_short_name method works"""
    short_name = f'{base_user.username}'
    assert base_user.get_short_name() == short_name


def test_base_user_email_is_normalized(base_user):
    """Test that a new user email is normalized"""
    email = 'estate@ESTATE.COM'
    assert base_user.email == email.lower()


def test_superuser_email_is_normalized(super_user):
    """Test that an admin user email is normalized"""
    email = 'estate@ESTATE.COM'
    assert super_user.email == email.lower()


def test_superuser_is_not_staff(user_factory):
    """Test that an error is raised when an admin user has is_staff set to false"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=False)
    assert str(err.value) == 'The superuser must have is_staff=True'


def test_superuser_is_not_superuser(user_factory):
    """Test that an error is raised when an admin user has is_superuser set to False"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=False, is_staff=True)
    assert str(err.value) == 'The superuser must have is_superuser=True'


def test_create_superuser_with_no_email(user_factory):
    """Test creating a superuser without an email address raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None, is_superuser=True, is_staff=True)
    assert str(err.value) == 'Must submit email'


def test_create_superuser_with_no_password(user_factory):
    """Test creating a superuser without a password raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=True, password=None)
    assert str(err.value) == 'The superuser must have password'


def test_create_user_with_no_email(user_factory):
    """Test that creating a new user with no email address raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None)
    assert str(err.value) == 'Must submit email'


def test_create_use_with_no_username(user_factory):
    """Test that creating a new user with no username raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(username=None)
    assert str(err.value) == 'Must submit a username'


def test_create_user_with_no_firstname(user_factory):
    """Test creating a new user without a first name raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(first_name=None)
    assert str(err.value) == 'Must submit a first_name'


def test_create_user_with_no_secondname(user_factory):
    """Test creating a new user without a second name raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(second_name=None)
    assert str(err.value) == 'Must submit a second_name'


def test_user_email_incorrect(user_factory):
    """Test that an Error is raised when a no valid email is provided"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email='estate.com')
    assert str(err.value) == 'Provide a valid email address'
