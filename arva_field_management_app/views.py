from django.shortcuts import render, redirect
from .forms import CSVUploadForm, FieldForm
from .models import Field, Client, ChannelPartner
import csv

# Create your views here.

def home(request):
    fields_exist = Field.objects.all().exists()

    return render(request, 'home.html', {'fields_exist': fields_exist})

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():

            csv_file = request.FILES['csv_file'] 
            #get file name
            file_name = csv_file.name
            #check if file is csv
            if not file_name.endswith('.csv'):
                form = CSVUploadForm()
                return render(request, 'upload_csv.html', {'form': form, 'error': 'Please upload a CSV file.'})
            #if file is too large, return
            if csv_file.multiple_chunks():
                form = CSVUploadForm()
                return render(request, 'upload_csv.html', {'form': form, 'error': 'Uploaded file is too big (%.2f MB).' % (csv_file.size/(1000*1000),)})
            
            #strip the .csv from the file name
            file_name = file_name[:-4]

            csv_data = csv.DictReader(csv_file.read().decode('utf-8-sig').splitlines())
            client, created = Client.objects.get_or_create(name=file_name)

            for row in csv_data:
                #ignore header row in csv case insensitive
                if row['field_name'].lower() == 'field_name':
                    continue

                print(row)
                Field.objects.create(
                    client=client,
                    field_name=row['field_name'],
                    field_location=row['field_location'],
                    acreage=row['acreage'],
                    field_type=row['field_type']
                )
            return redirect('browse_fields', client_id=client.id)
    else:
        form = CSVUploadForm()
    return render(request, 'upload_csv.html', {'form': form})

def browse_fields(request, client_id):
    client = Client.objects.get(id=client_id)
    fields = Field.objects.filter(client=client)
    return render(request, 'browse_fields.html', {'client': client, 'fields': fields})

def browse_clients(request):
    clients = Client.objects.all()
    return render(request, 'browse_clients.html', {'clients': clients})

def browse_channel_partners(request):
    channel_partners = ChannelPartner.objects.all()
    return render(request, 'browse_channel_partners.html', {'channel_partners': channel_partners})


def update_field(request, client_id, pk): 
    try:
        client = Client.objects.get(id=client_id)
        field = Field.objects.get(id=pk,client=client) 

        if request.method == 'POST':
            form = FieldForm(request.POST, instance=field)
            if form.is_valid():
                form.save()
                return redirect('browse_fields', client_id=client_id)
        else:
            form = FieldForm(instance=field)

        return render(request, 'update_field.html', {'client': client, 'form': form})
    except Field.DoesNotExist:
        #show message that the Field was not found
        return render(request, 'update_field.html', {'error': 'Field not found.'})
    
# Delete Field
def delete_field(request, client_id, pk):

    try:
        client = Client.objects.get(id=client_id)
        field = Field.objects.get(client=client,id=pk)
        if request.method == 'POST':
            field.delete()
            return redirect('browse_fields', client_id=client_id)
        return render(request, 'delete_field.html', {'client': client,'field': field})
    except Field.DoesNotExist:
        #show message that the Field was not found
        return render(request, 'delete_field.html', {'error': 'Field not found.'})
    
# Create Field
def create_field(request, client_id):
    client = Client.objects.get(id=client_id)
    form = FieldForm()
    if request.method == 'POST':
        form = FieldForm(request.POST)
        if form.is_valid():
            field = form.save(commit=False)
            field.client = client
            field.save()
            return redirect('browse_fields', client_id=client_id)
    else:
        form = FieldForm()

    return render(request, 'create_field.html', {'client': client, 'form': form})