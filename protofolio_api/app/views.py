from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View

class AboutView(View):
    def get(self, request):
        data = {
            "id": 1,
            "full_name": "Jane Doe",
            "title": "Full Stack Developer",
            "dob": "1998-05-15",
            "email": "janedoe@example.com",
            "contact": "+1234567890",
            "location": "New York, USA",
            "github_url": "https://github.com/janedoe",
            "linkedin_url": "https://linkedin.com/in/janedoe",
        }
        return JsonResponse(data)


class EducationView(View):
    def get(self, request):
        data = {
            "id": 1,
            "institution": "Tech University",
            "course": "B.Tech Computer Science",
            "university": "State University Board",
            "location": "California, USA",
            "startyear": 2016,
            "endyear": 2020,
            "grade": "8.8 CGPA",
            "description": "Graduated with honors in Software Engineering.",
        }
        return JsonResponse(data)


class ProjectsView(View):
    def get(self, request):
        projects_list = [
            {
                "id": 1,
                "projectname": "Portfolio Management API",
                "description": "REST endpoints serving developer portfolio information.",
                "technologies": ["Python", "Django", "JSON"],
                "duration": "2 weeks",
                "liveurl": "https://portfolio.example.com",
            },
            {
                "id": 2,
                "projectname": "E-Commerce App",
                "description": "An online storefront with cart and checkout features.",
                "technologies": ["Django", "PostgreSQL", "TailwindCSS"],
                "duration": "1 month",
                "liveurl": "https://shop.example.com",
            },
        ]
        return JsonResponse(projects_list, safe=False)