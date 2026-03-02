from routes.admin_routes import format_icon_class

def test_format_icon_class():
    assert format_icon_class('fa-heartbeat') == 'fas fa-heartbeat'
    assert format_icon_class('heartbeat') == 'fas fa-heartbeat'
    assert format_icon_class('fas fa-user') == 'fas fa-user'
    assert format_icon_class('fab fa-facebook') == 'fab fa-facebook'
    assert format_icon_class('far fa-clock') == 'far fa-clock'
    assert format_icon_class('') == ''
    assert format_icon_class(None) is None
    print("All format_icon_class tests passed!")

if __name__ == '__main__':
    test_format_icon_class()
