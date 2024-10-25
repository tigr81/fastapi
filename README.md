# fastapi

tigr81 FastAPI project template

## Development Workflow

### Steps to Contribute

1. **Make Changes**  
   Modify the template in `fastapi` as needed.

2. **Scaffold the Project Locally**  
   Use the following command to scaffold the project locally and verify that everything is functioning correctly:

    ```bash
    tigr81 scaffold fastapi --dev --default
    ```

3. **Commit Your Changes**
    Once you are satisfied with your modifications, commit your changes.

4. **Re-Scaffold the Project**
    Run the scaffold command again to ensure no changes are detected:

    ```bash
    tigr81 scaffold fastapi --dev --default
    ```

5. **Versioning Your Changes**
    Write a commit message following the format: release(`<type>`), where `<type>` is one of `major`, `minor`, or `patch`, to reflect the significance of the changes made.

6. **Create a Pull Request**
    Open a Pull Request (PR) from your branch to the main branch.

7. **Monitor the Release Process**
    After the PR is merged, close the PR and monitor the `Release on PR Merge` workflow to ensure the release is processed correctly.
