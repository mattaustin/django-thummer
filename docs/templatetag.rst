============
Template Tag
============
::

    {% load thummer %}
    
    {% thummer "http://www.example.com/" "400x400" as thumb %}
    <img src="{{ thumb.url }}" alt="" />
    {% endthummer %}

