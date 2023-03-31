Name:		texlive-comicneue
Version:	54891
Release:	2
Summary:	Use Comic Neue with TeX(-alike) systems
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/comicneue
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comicneue.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comicneue.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Comic Neue is a well-known redesign of the (in)famous Comic
Sans font. The package provides the original OpenType font for
XeTeX and LuaTeX users, and also has converted Type1 files for
pdfTeX users. Issues with this package can be reported on
GitHub or emailed to tex@slxh.nl.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/comicneue
%{_texmfdistdir}/fonts/vf/rozynski/comicneue
%{_texmfdistdir}/fonts/type1/rozynski/comicneue
%{_texmfdistdir}/fonts/tfm/rozynski/comicneue
%{_texmfdistdir}/fonts/opentype/rozynski/comicneue
%{_texmfdistdir}/fonts/map/dvips/comicneue
%{_texmfdistdir}/fonts/enc/dvips/comicneue
%doc %{_texmfdistdir}/doc/latex/comicneue

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
