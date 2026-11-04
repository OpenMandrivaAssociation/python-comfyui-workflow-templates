Name:		python-comfyui-workflow-templates
Version:	0.11.101
Release:	1
Summary:	ComfyUI workflow template bundle
License:	MIT
Group:		Development/Python
URL:		https://github.com/Comfy-Org/workflow_templates
Source0:	https://files.pythonhosted.org/packages/source/c/comfyui-workflow-templates/comfyui_workflow_templates-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

%description
Meta package for the official ComfyUI workflow templates.
ComfyUI 0.44.0 pins version 0.11.101. The workflows and preview
media live in the split packages this one requires.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/comfyui_workflow_templates
%{py_sitedir}/comfyui_workflow_templates-*.*-info
