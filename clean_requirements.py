import re

def clean_requirements(filename):
    with open(filename, 'r') as f:
        requirements = f.readlines()

    cleaned_requirements = []
    for req in requirements:
        # Remove lines with file paths or eggs
        if not re.search(r'(@file://|\.egg)', req):
            # Extract just the package name and version
            match = re.match(r'([^@\s]+)(?:@|==|>=|<=)?([\d.]+)?', req.strip())
            if match:
                package, version = match.groups()
                if version:
                    cleaned_requirements.append(f"{package}=={version}\n")
                else:
                    cleaned_requirements.append(f"{package}\n")

    with open(filename, 'w') as f:
        f.writelines(cleaned_requirements)

# Usage
clean_requirements('requirements.txt')