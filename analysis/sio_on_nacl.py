from spectral_cube import SpectralCube, wcs_utils, tests, Projection
from astropy import units as u
from astropy import wcs
from astropy.io import fits
import paths
import pylab as pl
import reproject

sourcename='SourceI'
robust = 0.5
linename='NaClv=2_26-25'
naclfn = paths.dpath('moments/Orion{1}_{0}_robust{robust}.maskedclarkclean10000_medsub_K_peak.fits').format(linename, sourcename, robust=robust)
linename='SiOv=0_8-7'
siov0fn = paths.dpath('moments/Orion{1}_{0}_robust{robust}.maskedclarkclean10000_medsub_K_peak.fits').format(linename, sourcename, robust=robust)
linename='SiOv=5_8-7'
siov5fn = paths.dpath('moments/Orion{1}_{0}_robust{robust}.maskedclarkclean10000_medsub_K_peak.fits').format(linename, sourcename, robust=robust)

siov0data = Projection.from_hdu(fits.open(siov0fn)[0])


mywcs = siov0data.wcs
pixscale = wcs.utils.proj_plane_pixel_area(mywcs)**0.5 * u.deg


imhalfsize = 0.2*u.arcsec
pixhs = (imhalfsize / pixscale).decompose().value
assert 1000 > pixhs > 10
cy, cx = siov0data.shape[0]/2., siov0data.shape[1]/2.
siov0data = siov0data[int(cy-pixhs):int(cy+pixhs), int(cx-pixhs):int(cx+pixhs)]

extent = [-siov0data.shape[1]/2*pixscale.to(u.arcsec).value,
          siov0data.shape[1]/2*pixscale.to(u.arcsec).value,
          -siov0data.shape[0]/2*pixscale.to(u.arcsec).value,
          siov0data.shape[0]/2*pixscale.to(u.arcsec).value,]

pl.figure(1).clf()
ax = pl.figure(1).gca()
im = ax.imshow(siov0data.value, cmap='gray_r',
               interpolation='none', origin='lower',
               extent=extent,
               zorder=0,
              )

nacldata,_ = reproject.reproject_interp(naclfn, siov0data.header)
ax.contour(nacldata, colors=['r']*3, levels=[200, ],
           extent=extent,
          )

siov5data,_ = reproject.reproject_interp(siov5fn, siov0data.header)
ax.contour(siov5data, colors=['b']*3, levels=[300, 400, 500, 600, 800],
           extent=extent,
          )

cb = pl.colorbar(mappable=im)
cb.set_label("$T_B$ [K]")
ax.set_xlabel("RA offset (\")")
ax.set_ylabel("Dec offset (\")")

pl.savefig(paths.fpath('SiO_8-7_on_NaClv=2_26-25.pdf'))
