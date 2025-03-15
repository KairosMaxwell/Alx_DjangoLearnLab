### Permissions and Groups Setup

- **Custom Permissions:**
  - Defined in `models.py` under the `Meta` class.
  - Permissions: `can_view`, `can_create`, `can_edit`, `can_delete`.

- **Groups:**
  - Created in Django admin: *Editors*, *Viewers*, *Admins*.
  - Permissions assigned:
    - **Editors:** `can_edit`, `can_create`
    - **Viewers:** `can_view`
    - **Admins:** All permissions.

- **Views:**
  - Permissions enforced using `@permission_required` and `PermissionRequiredMixin`.

- **Testing:**
  - Test users created and assigned to groups for manual verification of permissions.
