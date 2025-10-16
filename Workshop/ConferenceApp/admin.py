from django.contrib import admin
from .models import Conference, Submission
admin.site.site_header = "Gestion des conférences"
admin.site.site_title = "Admin Conférences"
admin.site.index_title = "Tableau de bord des conférences"

# Inline Stacked pour Submission
class SubmissionStackedInline(admin.StackedInline):
    model = Submission
    extra = 0
    fields = ("title", "abstract", "status", "submission_id", "submission_date")
    readonly_fields = ("submission_id", "submission_date")

# Inline Tabular pour Submission
class SubmissionTabularInline(admin.TabularInline):
    model = Submission
    extra = 0
    fields = ("title", "status", "user")

# Admin Conference
@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ("name", "theme", "start_date", "end_date", "duration")
    list_filter = ("theme", "start_date")
    search_fields = ("name", "description")
    ordering = ("start_date",)
    date_hierarchy = "start_date"
    fieldsets = (
        ("Informations générales", {
            "fields": ("name", "theme", "description")
        }),
        ("Logistique", {
            "fields": ("start_date", "end_date")
        }),
    )
    inlines = [SubmissionStackedInline, SubmissionTabularInline]

    def duration(self, obj):
        if obj.start_date and obj.end_date:
            return (obj.end_date - obj.start_date).days
        return "-"
    duration.short_description = "Durée (jours)"

# Admin Submission
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "user", "conference", "submission_date", "payed", "short_abstract")
    list_filter = ("status", "payed", "conference", "submission_date")
    search_fields = ("title", "keywords", "user__username")
    list_editable = ("status", "payed")
    readonly_fields = ("submission_id", "submission_date")
    fieldsets = (
        ("Infos générales", {
            "fields": ("submission_id", "title", "abstract", "keywords")
        }),
        ("Fichier et conférence", {
            "fields": ("paper", "conference")
        }),
        ("Suivi", {
            "fields": ("status", "payed", "submission_date", "user")
        }),
    )

    actions = ["mark_as_payed", "accept_submissions"]

    def short_abstract(self, obj):
        return (obj.abstract[:50] + "...") if obj.abstract and len(obj.abstract) > 50 else obj.abstract
    short_abstract.short_description = "Résumé court"

    def mark_as_payed(self, request, queryset):
        updated = queryset.update(payed=True)
        self.message_user(request, f"{updated} soumissions marquées comme payées.")
    mark_as_payed.short_description = "Marquer comme payées"

    def accept_submissions(self, request, queryset):
        updated = queryset.update(status="accepted")
        self.message_user(request, f"{updated} soumissions acceptées.")
    accept_submissions.short_description = "Accepter les soumissions"



