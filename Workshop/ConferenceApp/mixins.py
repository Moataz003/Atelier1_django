from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class CommitteeRequiredMixin(UserPassesTestMixin):

    # Vérifie si l'utilisateur est comité
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role == "comitee"

    # Si test_func = False
    def handle_no_permission(self):
        raise PermissionDenied("Vous n'avez pas les permissions nécessaires (réservé au comité).")
