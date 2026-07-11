%global tl_name hitszthesis
%global tl_revision 61073

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.2.1
Release:	%{tl_revision}.1
Summary:	A dissertation template for Harbin Institute of Technology, ShenZhen
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hitszthesis
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hitszthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hitszthesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hitszthesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a dissertation template for Harbin Institute of
Technology, ShenZhen (HITSZ), including bachelor, master and doctor
dissertations.

