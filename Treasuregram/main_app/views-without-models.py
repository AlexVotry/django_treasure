from django.shortcuts import render
from .models import Treasure

# Create your views here.
def index(request):
    # name = 'Gold Nugget'
    # value = 1000.00
    # context = { 'treasure_name': name,
    #             'treasure_val': value }

    # if we used the above lines, we would pass in context instead of { 'treasures': treasures }
    treasures = Treasure.objects.all()
    return render(request, 'index.html', { 'treasures': treasures })

# This all gets replaced with the models.py
class Treasure:
    def __init__(self, name, value, material, location):
        self.name = name
        self.value = value
        self.material = material
        self.location = location

treasures = [
    Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM"),
    Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO"),
    Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA')
]
