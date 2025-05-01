"""test_one_plugin plugin for Pollination."""

docker_registry = 'https://mcr.microsoft.com';
docker_image_id = "mcr.microsoft.com/powershell:alpine-3.20";
docker_work_dir = "/home";

__pollination__ = {
    'config': {
        'docker': {
            'image': docker_image_id,
            'workdir': docker_work_dir,
            'registry': docker_registry,
        }
    }
};