Name:		texlive-hitszthesis
Version:	61073
Release:	2
Summary:	A dissertation template for Harbin Institute of Technology, ShenZhen
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hitszthesis
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hitszthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hitszthesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hitszthesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a dissertation template for Harbin
Institute of Technology, ShenZhen (HITSZ), including bachelor,
master and doctor dissertations.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hitszthesis
%{_texmfdistdir}/tex/latex/hitszthesis
%{_texmfdistdir}/makeindex/hitszthesis
%{_texmfdistdir}/bibtex/bst/hitszthesis
%doc %{_texmfdistdir}/doc/latex/hitszthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
