from cmath import sqrt, log, pi

from ..parameters import alpha_em
from ..parameters import pion_mass_chiral_limit as mPI
from ..parameters import kaon_mass_chiral_limit as mK
from ..parameters import rho_mass as mrho
from ..parameters import rho_width
from ..parameters import fpi, fv, gv, qe, vh

from ..unitarization.bethe_salpeter import amp_kk_to_kk_bse
from ..unitarization.bethe_salpeter import amp_pipi_to_kk_bse
from ..unitarization.bethe_salpeter import amp_pipi_to_pipi_bse
from ..unitarization.loops import bubble_loop


def __xx_s_pipig_no_rho_5_bub_E(Q, s, t, params):
    gsxx = params.gsxx
    gsGG = params.gsGG
    gsff = params.gsff
    mx = params.mx
    ms = params.ms
    vs = params.vs

    return (complex(0., 0.0051440329218107)*gsxx*sqrt(-4.*mx**2 + Q**2)*qe *
            (6. *
             (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
              2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                       mK**2 *
                       (81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2))) *
             amp_kk_to_kk_bse(Q)*bubble_loop(Q, mK)**2 +
             12. *
             (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
              2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                       mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs
                               - 64.*gsGG**2*vs**2))) *
             bubble_loop(Q, mPI)*(-1. +
                                  amp_pipi_to_pipi_bse(Q) *
                                  bubble_loop(Q, mPI)) +
             bubble_loop(Q, mK) *
             (8.*sqrt(3.) *
              (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
               2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                        mK**2*(81.*vh**2 - 144.*gsGG*vh*vs -
                               64.*gsGG**2*vs**2))) *
              amp_pipi_to_kk_bse(Q) * bubble_loop(Q, mPI) +
              3.*(-2.*(9.*gsff*(18.*gsGG*Q**2*vh*vs +
                                mK**2*(9.*vh + 8.*gsGG*vs)**2) +
                       2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs -
                                       64.*gsGG**2*vs**2))) +
                  sqrt(3.)*(9.*gsff*(18.*gsGG*Q**2*vh*vs +
                                     mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
                            2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                                     mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs -
                                             64.*gsGG**2*vs**2))) *
                  amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mPI))))) / \
        (sqrt(2.)*fpi**2*(ms - Q)*(ms + Q)*vh *
         (3.*vh + 3.*gsff*vs + 2.*gsGG*vs) * (9.*vh + 4.*gsGG*vs))


def __xx_s_pipig_no_rho_fsr_bub_E(Q, s, t, params):
    gsxx = params.gsxx
    gsGG = params.gsGG
    gsff = params.gsff
    mx = params.mx
    ms = params.ms
    vs = params.vs

    return (complex(0., 0.00205761316872428)*gsxx*sqrt(-4.*mx**2 + Q**2)*qe *
            (6.*(mPI**2 + 3.*Q**2 - t) *
             (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
              2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                       mK**2*(81.*vh**2 - 144.*gsGG*vh*vs -
                              64.*gsGG**2*vs**2))) *
             bubble_loop(Q, mK) - 6.*(mPI**2 + 3.*Q**2 - t) *
             (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
              2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                       mK**2*(81.*vh**2 - 144.*gsGG*vh*vs -
                              64.*gsGG**2*vs**2))) *
             amp_kk_to_kk_bse(Q)*bubble_loop(Q, mK)**2 -
             6.*(mPI**2 - 6.*Q**2 + 2.*t) *
             (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
              2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                       mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs -
                               64.*gsGG**2*vs**2))) *
             bubble_loop(Q, mPI) + 4.*sqrt(3.)*(mPI**2 - 6.*Q**2 + 2.*t) *
             (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
              2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                       mK**2*(81.*vh**2 - 144.*gsGG*vh*vs -
                              64.*gsGG**2*vs**2))) *
             amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK) *
             bubble_loop(Q, mPI) - 3.*sqrt(3.)*(mPI**2 + 3.*Q**2 - t) *
             (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
              2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                       mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs -
                               64.*gsGG**2*vs**2))) *
             amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK) *
             bubble_loop(Q, mPI) + 6.*(mPI**2 - 6.*Q**2 + 2.*t) *
             (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
              2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                       mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs -
                               64.*gsGG**2*vs**2))) *
             amp_pipi_to_pipi_bse(Q)*bubble_loop(Q, mPI)**2)) / \
            (sqrt(2.)*fpi**2*(ms - Q)*(ms + Q)*(mPI**2 - t)*vh *
             (3.*vh + 3.*gsff*vs + 2.*gsGG*vs)*(9.*vh + 4.*gsGG*vs))


def __xx_s_pipig_no_rho_no_bub_E(Q, s, t, params):
    gsxx = params.gsxx
    gsGG = params.gsGG
    gsff = params.gsff
    mx = params.mx
    ms = params.ms
    vs = params.vs

    return (complex(0., 0.012345679012345678)*gsxx*sqrt(-4.*mx**2 + Q**2)*qe*
        ((-2.*(-2.*fv*gsGG*gv*(mPI**2 - t)*(mPI**2 + Q**2 - s - t)*
                (3.*vh + 3.*gsff*vs + 2.*gsGG*vs)*
                (81.*vh**2 + 54.*gsGG*vh*vs + 8.*gsGG**2*vs**2) +
               3.*fpi**2*mrhoT**2*vh*
                (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
                  2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                     mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))))/
           (mrhoT**2*(mPI**2 - t)*vh**2*(3.*vh + 3.*gsff*vs + 2.*gsGG*vs)) +
          (5184.*gsGG*mK**2*pi**4*(mPI**2 - u)*bubble_loop(0., mK))/
           (-2.*mPI**2 + t + u) + (10368.*gsGG*mPI**2*pi**4*(mPI**2 - u)*
             bubble_loop(0., mPI))/(-2.*mPI**2 + t + u) -
          (48.*pi**4*(gsGG*(-9.*(24.*mPI**6 - 6.*s**2*t - 8.*s*t**2 - 3.*t**3 -
                     12.*s**2*u - 22.*s*t*u - 9.*t**2*u - 14.*s*u**2 -
                     9.*t*u**2 - 3.*u**3 + 3.*Q**2*(t + u)*(2.*s + t + u) +
                     4.*mPI**4*(3.*Q**2 - 11.*s - 9.*(t + u)) -
                     2.*mPI**2*(-9.*s**2 - 9.*(t + u)**2 +
                        6.*Q**2*(s + t + u) - s*(19.*t + 25.*u)))*vh*
                   (3.*vh + 2.*gsGG*vs) +
                  2.*mK**2*(81.*s*t*vh**2 + 135.*t**2*vh**2 + 162.*s*u*vh**2 +
                     270.*t*u*vh**2 + 135.*u**2*vh**2 - 144.*gsGG*s*t*vh*vs -
                     108.*gsGG*t**2*vh*vs - 288.*gsGG*s*u*vh*vs -
                     216.*gsGG*t*u*vh*vs - 108.*gsGG*u**2*vh*vs -
                     64.*gsGG**2*s*t*vs**2 - 64.*gsGG**2*t**2*vs**2 -
                     128.*gsGG**2*s*u*vs**2 - 128.*gsGG**2*t*u*vs**2 -
                     64.*gsGG**2*u**2*vs**2 -
                     Q**2*(t + u)*
                      (81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2) +
                     4.*mPI**4*(135.*vh**2 - 108.*gsGG*vh*vs -
                        64.*gsGG**2*vs**2) +
                     mPI**2*(2.*Q**2*
                         (81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2) -
                        4.*(t + u)*
                         (135.*vh**2 - 108.*gsGG*vh*vs - 64.*gsGG**2*vs**2) +
                        3.*s*(-81.*vh**2 + 144.*gsGG*vh*vs + 64.*gsGG**2*vs**2)))) + 9.*gsff*(-3.*gsGG*(24.*mPI**6 - 6.*s**2*t - 8.*s*t**2 - 3.*t**3 -
                     12.*s**2*u - 22.*s*t*u - 9.*t**2*u - 14.*s*u**2 -
                     9.*t*u**2 - 3.*u**3 + 3.*Q**2*(t + u)*(2.*s + t + u) +
                     4.*mPI**4*(3.*Q**2 - 11.*s - 9.*(t + u)) -
                     2.*mPI**2*(-9.*s**2 - 9.*(t + u)**2 +
                        6.*Q**2*(s + t + u) - s*(19.*t + 25.*u)))*vh*vs +
                  mK**2*(81.*s*t*vh**2 + 81.*t**2*vh**2 + 162.*s*u*vh**2 +
                     162.*t*u*vh**2 + 81.*u**2*vh**2 + 144.*gsGG*s*t*vh*vs +
                     156.*gsGG*t**2*vh*vs + 288.*gsGG*s*u*vh*vs +
                     312.*gsGG*t*u*vh*vs + 156.*gsGG*u**2*vh*vs +
                     64.*gsGG**2*s*t*vs**2 + 64.*gsGG**2*t**2*vs**2 +
                     128.*gsGG**2*s*u*vs**2 + 128.*gsGG**2*t*u*vs**2 +
                     64.*gsGG**2*u**2*vs**2 -
                     Q**2*(t + u)*(9.*vh + 8.*gsGG*vs)**2 +
                     4.*mPI**4*(81.*vh**2 + 156.*gsGG*vh*vs +
                        64.*gsGG**2*vs**2) +
                     mPI**2*(2.*Q**2*(9.*vh + 8.*gsGG*vs)**2 -
                        3.*s*(9.*vh + 8.*gsGG*vs)**2 -
                        4.*(t + u)*
                         (81.*vh**2 + 156.*gsGG*vh*vs + 64.*gsGG**2*vs**2)))))*
             bubble_loop(sqrt(s), mK))/
           ((-2.*mPI**2 + t + u)**2*vh*(3.*vh + 3.*gsff*vs + 2.*gsGG*vs)) -
          (96.*pi**4*(9.*gsff*(3.*gsGG*
                   (3.*(t + u)**3 - 3.*Q**2*(t + u)*(2.*s + t + u) +
                     6.*s**2*(t + 2.*u) + 2.*s*(4.*t**2 + 11.*t*u + 7.*u**2))*vh*
                   vs + 4.*mPI**6*
                   (81.*vh**2 + 138.*gsGG*vh*vs + 64.*gsGG**2*vs**2) +
                  mPI**4*(-3.*s*(81.*vh**2 + 100.*gsGG*vh*vs +
                        64.*gsGG**2*vs**2) +
                     2.*Q**2*(81.*vh**2 + 126.*gsGG*vh*vs +
                        64.*gsGG**2*vs**2) -
                     4.*(t + u)*(81.*vh**2 + 129.*gsGG*vh*vs +
                        64.*gsGG**2*vs**2)) +
                  mPI**2*(-54.*gsGG*s**2*vh*vs +
                     (t + u)**2*(81.*vh**2 + 102.*gsGG*vh*vs +
                        64.*gsGG**2*vs**2) +
                     s*(t*(81.*vh**2 + 30.*gsGG*vh*vs + 64.*gsGG**2*vs**2) +
                        2.*u*(81.*vh**2 + 69.*gsGG*vh*vs + 64.*gsGG**2*vs**2)) \
    - Q**2*(81.*u*vh**2 - 36.*gsGG*s*vh*vs + 108.*gsGG*u*vh*vs +
                        64.*gsGG**2*u*vs**2 +
                        t*(81.*vh**2 + 108.*gsGG*vh*vs + 64.*gsGG**2*vs**2)))) +
                      gsGG*(-9.*(-3.*(t + u)**3 + 3.*Q**2*(t + u)*(2.*s + t + u) -
                     6.*s**2*(t + 2.*u) - 2.*s*(4.*t**2 + 11.*t*u + 7.*u**2))*vh*
                   (3.*vh + 2.*gsGG*vs) +
                  16.*mPI**6*(27.*vh**2 - 81.*gsGG*vh*vs - 32.*gsGG**2*vs**2) +
                  2.*mPI**4*(-54.*u*vh**2 - 396.*gsGG*Q**2*vh*vs +
                     756.*gsGG*u*vh*vs - 128.*gsGG**2*Q**2*vs**2 +
                     256.*gsGG**2*u*vs**2 +
                     3.*s*(117.*vh**2 + 276.*gsGG*vh*vs + 64.*gsGG**2*vs**2) +
                     t*(-54.*vh**2 + 756.*gsGG*vh*vs + 256.*gsGG**2*vs**2)) +
                  2.*mPI**2*(-81.*s**2*vh*(3.*vh + 2.*gsGG*vs) -
                     2.*(t + u)**2*
                      (54.*vh**2 + 135.*gsGG*vh*vs + 32.*gsGG**2*vs**2) -
                     s*(432.*t*vh**2 + 513.*u*vh**2 + 486.*gsGG*t*vh*vs +
                        738.*gsGG*u*vh*vs + 64.*gsGG**2*t*vs**2 +
                        128.*gsGG**2*u*vs**2) +
                     Q**2*(54.*s*vh*(3.*vh + 2.*gsGG*vs) +
                        (t + u)*(81.*vh**2 + 252.*gsGG*vh*vs +
                           64.*gsGG**2*vs**2)))))*bubble_loop(sqrt(s), mPI))/
           ((-2.*mPI**2 + t + u)**2*vh*(3.*vh + 3.*gsff*vs + 2.*gsGG*vs)) -
          (24.*pi**4*(12.*mPI**4 + 2.*s*t + 3.*t**2 + 4.*s*u + 6.*t*u + 3.*u**2 -
               2.*Q**2*(t + u) + 2.*mPI**2*(2.*Q**2 - 3.*(s + 2.*(t + u))))*
             (-9.*gsff*(18.*gsGG*(-2.*mPI**2 + s + t + u)*vh*vs +
                  mK**2*(9.*vh + 8.*gsGG*vs)**2) +
               2.*gsGG*(27.*(2.*mPI**2 - s - t - u)*vh*(3.*vh + 2.*gsGG*vs) +
                  mK**2*(-81.*vh**2 + 144.*gsGG*vh*vs + 64.*gsGG**2*vs**2)))*
             bubble_loop(sqrt(-2.*mPI**2 + s + t + u), mK))/
           ((-2.*mPI**2 + t + u)**2*vh*(3.*vh + 3.*gsff*vs + 2.*gsGG*vs)) +
          (48.*pi**4*(12.*mPI**4 + 2.*s*t + 3.*t**2 + 4.*s*u + 6.*t*u + 3.*u**2 -
               2.*Q**2*(t + u) + 2.*mPI**2*(2.*Q**2 - 3.*(s + 2.*(t + u))))*
             (9.*gsff*(18.*gsGG*(s + t + u)*vh*vs +
                  mPI**2*(81.*vh**2 + 108.*gsGG*vh*vs + 64.*gsGG**2*vs**2)) -
               2.*gsGG*(-27.*(s + t + u)*vh*(3.*vh + 2.*gsGG*vs) +
                  mPI**2*(81.*vh**2 + 252.*gsGG*vh*vs + 64.*gsGG**2*vs**2)))*
             bubble_loop(sqrt(-2.*mPI**2 + s + t + u), mPI))/
           ((-2.*mPI**2 + t + u)**2*vh*(3.*vh + 3.*gsff*vs + 2.*gsGG*vs)) -
          (216.*gsGG*mK**2*pi**2*(mPI**2 - 2.*t + u)*
             log((qmax + sqrt(mK**2 + qmax**2))/mK))/(-2.*mPI**2 + t + u) -
          (432.*gsGG*mPI**2*pi**2*(mPI**2 - 2.*t + u)*
             log((qmax + sqrt(mPI**2 + qmax**2))/mPI))/(-2.*mPI**2 + t + u) -
          (3.*mK**2*pi**2*(mPI**2 - u)*
             (9.*gsff*(18.*gsGG*(-2.*mPI**2 + s + t + u)*vh*vs +
                  mK**2*(9.*vh + 8.*gsGG*vs)**2) -
               2.*gsGG*(27.*(2.*mPI**2 - s - t - u)*vh*(3.*vh + 2.*gsGG*vs) +
                  mK**2*(-81.*vh**2 + 144.*gsGG*vh*vs + 64.*gsGG**2*vs**2)))*
             log((2.*mK**2 - s + sqrt(s*(-4.*mK**2 + s)))/(2.*mK**2))**2)/
           ((-2.*mPI**2 + t + u)**2*vh*(3.*vh + 3.*gsff*vs + 2.*gsGG*vs)) -
          (6.*mPI**2*pi**2*(mPI**2 - u)*
             (9.*gsff*(18.*gsGG*(s + t + u)*vh*vs +
                  mPI**2*(81.*vh**2 + 108.*gsGG*vh*vs + 64.*gsGG**2*vs**2)) -
               2.*gsGG*(-27.*(s + t + u)*vh*(3.*vh + 2.*gsGG*vs) +
                  mPI**2*(81.*vh**2 + 252.*gsGG*vh*vs + 64.*gsGG**2*vs**2)))*
             log((2.*mPI**2 - s + sqrt(s*(-4.*mPI**2 + s)))/(2.*mPI**2))**2)/
           ((-2.*mPI**2 + t + u)**2*vh*(3.*vh + 3.*gsff*vs + 2.*gsGG*vs)) +
          (6.*mPI**2*pi**2*(mPI**2 - u)*
             (9.*gsff*(18.*gsGG*(s + t + u)*vh*vs +
                  mPI**2*(81.*vh**2 + 108.*gsGG*vh*vs + 64.*gsGG**2*vs**2)) -
               2.*gsGG*(-27.*(s + t + u)*vh*(3.*vh + 2.*gsGG*vs) +
                  mPI**2*(81.*vh**2 + 252.*gsGG*vh*vs + 64.*gsGG**2*vs**2)))*
             log(-(-4.*mPI**2 + s + t + u -
                   sqrt((-6.*mPI**2 + s + t + u)*(-2.*mPI**2 + s + t + u)))/
                (2.*mPI**2))**2)/
           ((-2.*mPI**2 + t + u)**2*vh*(3.*vh + 3.*gsff*vs + 2.*gsGG*vs)) +
          (3.*mK**2*pi**2*(mPI**2 - u)*
             (9.*gsff*(18.*gsGG*(-2.*mPI**2 + s + t + u)*vh*vs +
                  mK**2*(9.*vh + 8.*gsGG*vs)**2) -
               2.*gsGG*(27.*(2.*mPI**2 - s - t - u)*vh*(3.*vh + 2.*gsGG*vs) +
                  mK**2*(-81.*vh**2 + 144.*gsGG*vh*vs + 64.*gsGG**2*vs**2)))*
             log(-(-2.*mK**2 - 2.*mPI**2 + s + t + u -
                   sqrt((-2.*mPI**2 + s + t + u)*
                     (-4.*mK**2 - 2.*mPI**2 + s + t + u)))/(2.*mK**2))**2) /
           ((-2.*mPI**2 + t + u)**2*vh*(3.*vh + 3.*gsff*vs + 2.*gsGG*vs)))) / \
      (sqrt(2.)*fpi**2*(ms - Q)*(ms + Q)*(9.*vh + 4.*gsGG*vs))


def __xx_s_pipig_no_rho_triangle_bub_E(Q, s, t, params):
    gsxx = params.gsxx
    gsGG = params.gsGG
    gsff = params.gsff
    mx = params.mx
    ms = params.ms
    vs = params.vs

    return (complex(0., 0.00017146776406035664)*gsxx*pi**2*sqrt(-4.*mx**2 + Q**2)*qe*
        (1728.*mK**2*pi**2*(Q**2 - s)*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(0., mK)*bubble_loop(Q, mK) +
          2304.*mPI**2*pi**2*(Q**2 - s)*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(0., mPI)*bubble_loop(Q, mK) -
          1296.*pi**2*Q**2*(Q**4 - s*(-2.*mPI**2 + s + 2.*t))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mK)**2 - 1728.*mK**2*pi**2*(Q**2 - s)*
           (mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_kk_to_kk_bse(Q)*bubble_loop(0., mK)*bubble_loop(Q, mK)**2 -
          2304.*mPI**2*pi**2*(Q**2 - s)*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_kk_to_kk_bse(Q)*bubble_loop(0., mPI)*bubble_loop(Q, mK)**2 +
          1296.*pi**2*Q**2*(Q**4 - s*(-2.*mPI**2 + s + 2.*t))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_kk_to_kk_bse(Q)*bubble_loop(Q, mK)**3 +
          864.*mK**2*pi**2*(Q**2 - s)*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(0., mK)*bubble_loop(Q, mPI) +
          4608.*mPI**2*pi**2*(Q**2 - s)*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(0., mPI)*bubble_loop(Q, mPI) -
          216.*pi**2*Q**2*(Q**4 - s*(-2.*mPI**2 + s + 2.*t))*
           (9.*gsff*(8.*mK**2*(9.*vh + 8.*gsGG*vs)**2 +
                3.*(66.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2)) -
             2.*gsGG*(-8.*mK**2*(81.*vh**2 - 144.*gsGG*vh*vs -
                   64.*gsGG**2*vs**2) +
                3.*(-99.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                   mPI**2*(-81.*vh**2 + 144.*gsGG*vh*vs + 64.*gsGG**2*vs**2))))*
           bubble_loop(Q, mK)*bubble_loop(Q, mPI) -
          576.*sqrt(3.)*mK**2*pi**2*(Q**2 - s)*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(0., mK)*bubble_loop(Q, mK)*
           bubble_loop(Q, mPI) - 864.*sqrt(3.)*mK**2*pi**2*(Q**2 - s)*
           (mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(0., mK)*bubble_loop(Q, mK)*
           bubble_loop(Q, mPI) - 3072.*sqrt(3.)*mPI**2*pi**2*(Q**2 - s)*
           (mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(0., mPI)*bubble_loop(Q, mK)*
           bubble_loop(Q, mPI) - 1152.*sqrt(3.)*mPI**2*pi**2*(Q**2 - s)*
           (mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(0., mPI)*bubble_loop(Q, mK)*
           bubble_loop(Q, mPI) + 1728.*pi**2*Q**2*
           (Q**4 - s*(-2.*mPI**2 + s + 2.*t))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_kk_to_kk_bse(Q)*bubble_loop(Q, mK)**2*bubble_loop(Q, mPI) +
          432.*sqrt(3.)*pi**2*Q**2*(Q**4 - s*(-2.*mPI**2 + s + 2.*t))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)**2*bubble_loop(Q, mPI) +
          648.*sqrt(3.)*pi**2*Q**2*(Q**4 - s*(-2.*mPI**2 + s + 2.*t))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)**2*bubble_loop(Q, mPI) +
          1728.*pi**2*(mPI**2 - 2.*Q**2)*(Q**4 - s*(-2.*mPI**2 + s + 2.*t))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mPI)**2 - 864.*mK**2*pi**2*(Q**2 - s)*
           (mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_pipi_bse(Q)*bubble_loop(0., mK)*bubble_loop(Q, mPI)**2 \
    - 4608.*mPI**2*pi**2*(Q**2 - s)*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_pipi_bse(Q)*bubble_loop(0., mPI)*bubble_loop(Q, mPI)**2 \
    - 1152.*sqrt(3.)*pi**2*(mPI**2 - 2.*Q**2)*(Q**4 - s*(-2.*mPI**2 + s + 2.*t))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)**2 +
          864.*sqrt(3.)*pi**2*Q**2*(Q**4 - s*(-2.*mPI**2 + s + 2.*t))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)**2 +
          648.*pi**2*Q**2*(Q**4 - s*(-2.*mPI**2 + s + 2.*t))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_pipi_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)**2 \
    - 1728.*pi**2*(mPI**2 - 2.*Q**2)*(Q**4 - s*(-2.*mPI**2 + s + 2.*t))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_pipi_bse(Q)*bubble_loop(Q, mPI)**3 +
          144.*pi**2*(4.*mK**2*(Q**2 - s)**2 -
             s*(-18.*mPI**2*Q**2 - 17.*Q**4 + s**2 + 2.*Q**2*(8.*s + 9.*t)))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mK)*bubble_loop(sqrt(s), mK) -
          144.*pi**2*(4.*mK**2*(Q**2 - s)**2 -
             s*(-18.*mPI**2*Q**2 - 17.*Q**4 + s**2 + 2.*Q**2*(8.*s + 9.*t)))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_kk_to_kk_bse(Q)*bubble_loop(Q, mK)**2*
           bubble_loop(sqrt(s), mK) +
          72.*pi**2*(4.*mK**2*(Q**2 - s)**2 -
             s*(-18.*mPI**2*Q**2 - 17.*Q**4 + s**2 + 2.*Q**2*(8.*s + 9.*t)))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mPI)*bubble_loop(sqrt(s), mK) -
          48.*sqrt(3.)*pi**2*(4.*mK**2*(Q**2 - s)**2 -
             s*(-18.*mPI**2*Q**2 - 17.*Q**4 + s**2 + 2.*Q**2*(8.*s + 9.*t)))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)*
           bubble_loop(sqrt(s), mK) -
          72.*sqrt(3.)*pi**2*(4.*mK**2*(Q**2 - s)**2 -
             s*(-18.*mPI**2*Q**2 - 17.*Q**4 + s**2 + 2.*Q**2*(8.*s + 9.*t)))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)*
           bubble_loop(sqrt(s), mK) -
          72.*pi**2*(4.*mK**2*(Q**2 - s)**2 -
             s*(-18.*mPI**2*Q**2 - 17.*Q**4 + s**2 + 2.*Q**2*(8.*s + 9.*t)))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_pipi_bse(Q)*bubble_loop(Q, mPI)**2*
           bubble_loop(sqrt(s), mK) +
          192.*pi**2*(2.*mPI**2*(2.*Q**4 + 5.*Q**2*s + 2.*s**2) -
             s*(-17.*Q**4 + s**2 + 2.*Q**2*(8.*s + 9.*t)))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mK)*bubble_loop(sqrt(s), mPI) -
          192.*pi**2*(2.*mPI**2*(2.*Q**4 + 5.*Q**2*s + 2.*s**2) -
             s*(-17.*Q**4 + s**2 + 2.*Q**2*(8.*s + 9.*t)))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_kk_to_kk_bse(Q)*bubble_loop(Q, mK)**2*
           bubble_loop(sqrt(s), mPI) +
          384.*pi**2*(-9.*mPI**4*s - s*(-17.*Q**4 + s**2 + 2.*Q**2*(8.*s + 9.*t)) +
             mPI**2*(4.*Q**4 + Q**2*s + s*(13.*s + 9.*t)))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mPI)*bubble_loop(sqrt(s), mPI) +
          256.*sqrt(3.)*pi**2*(9.*mPI**4*s +
             s*(-17.*Q**4 + s**2 + 2.*Q**2*(8.*s + 9.*t)) -
             mPI**2*(4.*Q**4 + Q**2*s + s*(13.*s + 9.*t)))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)*
           bubble_loop(sqrt(s), mPI) -
          96.*sqrt(3.)*pi**2*(2.*mPI**2*(2.*Q**4 + 5.*Q**2*s + 2.*s**2) -
             s*(-17.*Q**4 + s**2 + 2.*Q**2*(8.*s + 9.*t)))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)*
           bubble_loop(sqrt(s), mPI) +
          384.*pi**2*(9.*mPI**4*s + s*(-17.*Q**4 + s**2 + 2.*Q**2*(8.*s + 9.*t)) -
             mPI**2*(4.*Q**4 + Q**2*s + s*(13.*s + 9.*t)))*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_pipi_bse(Q)*bubble_loop(Q, mPI)**2*
           bubble_loop(sqrt(s), mPI) +
          162.*mK**2*Q**2*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mK)*log((2.*mK**2 + Q*(-Q + sqrt(-4.*mK**2 + Q**2)))/
              (2.*mK**2))**2 - 162.*mK**2*Q**2*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_kk_to_kk_bse(Q)*bubble_loop(Q, mK)**2*
           log((2.*mK**2 + Q*(-Q + sqrt(-4.*mK**2 + Q**2)))/(2.*mK**2))**2 +
          81.*mK**2*Q**2*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mPI)*log((2.*mK**2 + Q*(-Q + sqrt(-4.*mK**2 + Q**2)))/
              (2.*mK**2))**2 - 54.*sqrt(3.)*mK**2*Q**2*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)*
           log((2.*mK**2 + Q*(-Q + sqrt(-4.*mK**2 + Q**2)))/(2.*mK**2))**2 -
          81.*sqrt(3.)*mK**2*Q**2*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)*
           log((2.*mK**2 + Q*(-Q + sqrt(-4.*mK**2 + Q**2)))/(2.*mK**2))**2 -
          81.*mK**2*Q**2*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_pipi_bse(Q)*bubble_loop(Q, mPI)**2*
           log((2.*mK**2 + Q*(-Q + sqrt(-4.*mK**2 + Q**2)))/(2.*mK**2))**2 +
          216.*mPI**2*Q**2*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mK)*log((2.*mPI**2 + Q*(-Q + sqrt(-4.*mPI**2 + Q**2)))/
              (2.*mPI**2))**2 - 216.*mPI**2*Q**2*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_kk_to_kk_bse(Q)*bubble_loop(Q, mK)**2*
           log((2.*mPI**2 + Q*(-Q + sqrt(-4.*mPI**2 + Q**2)))/(2.*mPI**2))**2 -
          216.*mPI**2*(mPI**2 - 2.*Q**2)*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mPI)*log((2.*mPI**2 + Q*(-Q + sqrt(-4.*mPI**2 + Q**2)))/
              (2.*mPI**2))**2 + 144.*sqrt(3.)*mPI**2*(mPI**2 - 2.*Q**2)*
           (mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)*
           log((2.*mPI**2 + Q*(-Q + sqrt(-4.*mPI**2 + Q**2)))/(2.*mPI**2))**2 -
          108.*sqrt(3.)*mPI**2*Q**2*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)*
           log((2.*mPI**2 + Q*(-Q + sqrt(-4.*mPI**2 + Q**2)))/(2.*mPI**2))**2 +
          216.*mPI**2*(mPI**2 - 2.*Q**2)*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_pipi_bse(Q)*bubble_loop(Q, mPI)**2*
           log((2.*mPI**2 + Q*(-Q + sqrt(-4.*mPI**2 + Q**2)))/(2.*mPI**2))**2 +
          72.*mK**2*(Q**2 - s)*(3.*mPI**2 + Q**2 - s - 3.*t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mK)*log((qmax + sqrt(mK**2 + qmax**2))/mK) -
          72.*mK**2*(Q**2 - s)*(3.*mPI**2 + Q**2 - s - 3.*t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_kk_to_kk_bse(Q)*bubble_loop(Q, mK)**2*
           log((qmax + sqrt(mK**2 + qmax**2))/mK) +
          36.*mK**2*(Q**2 - s)*(3.*mPI**2 + Q**2 - s - 3.*t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mPI)*log((qmax + sqrt(mK**2 + qmax**2))/mK) -
          24.*sqrt(3.)*mK**2*(Q**2 - s)*(3.*mPI**2 + Q**2 - s - 3.*t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)*
           log((qmax + sqrt(mK**2 + qmax**2))/mK) -
          36.*sqrt(3.)*mK**2*(Q**2 - s)*(3.*mPI**2 + Q**2 - s - 3.*t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)*
           log((qmax + sqrt(mK**2 + qmax**2))/mK) -
          36.*mK**2*(Q**2 - s)*(3.*mPI**2 + Q**2 - s - 3.*t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_pipi_bse(Q)*bubble_loop(Q, mPI)**2*
           log((qmax + sqrt(mK**2 + qmax**2))/mK) +
          96.*mPI**2*(Q**2 - s)*(3.*mPI**2 + Q**2 - s - 3.*t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mK)*log((qmax + sqrt(mPI**2 + qmax**2))/mPI) -
          96.*mPI**2*(Q**2 - s)*(3.*mPI**2 + Q**2 - s - 3.*t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_kk_to_kk_bse(Q)*bubble_loop(Q, mK)**2*
           log((qmax + sqrt(mPI**2 + qmax**2))/mPI) +
          192.*mPI**2*(Q**2 - s)*(3.*mPI**2 + Q**2 - s - 3.*t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mPI)*log((qmax + sqrt(mPI**2 + qmax**2))/mPI) -
          128.*sqrt(3.)*mPI**2*(Q**2 - s)*(3.*mPI**2 + Q**2 - s - 3.*t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)*
           log((qmax + sqrt(mPI**2 + qmax**2))/mPI) -
          48.*sqrt(3.)*mPI**2*(Q**2 - s)*(3.*mPI**2 + Q**2 - s - 3.*t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)*
           log((qmax + sqrt(mPI**2 + qmax**2))/mPI) -
          192.*mPI**2*(Q**2 - s)*(3.*mPI**2 + Q**2 - s - 3.*t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_pipi_bse(Q)*bubble_loop(Q, mPI)**2*
           log((qmax + sqrt(mPI**2 + qmax**2))/mPI) -
          162.*mK**2*Q**2*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mK)*log((2.*mK**2 - s + sqrt(s*(-4.*mK**2 + s)))/
              (2.*mK**2))**2 + 162.*mK**2*Q**2*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_kk_to_kk_bse(Q)*bubble_loop(Q, mK)**2*
           log((2.*mK**2 - s + sqrt(s*(-4.*mK**2 + s)))/(2.*mK**2))**2 -
          81.*mK**2*Q**2*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mPI)*log((2.*mK**2 - s + sqrt(s*(-4.*mK**2 + s)))/
              (2.*mK**2))**2 + 54.*sqrt(3.)*mK**2*Q**2*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)*
           log((2.*mK**2 - s + sqrt(s*(-4.*mK**2 + s)))/(2.*mK**2))**2 +
          81.*sqrt(3.)*mK**2*Q**2*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)*
           log((2.*mK**2 - s + sqrt(s*(-4.*mK**2 + s)))/(2.*mK**2))**2 +
          81.*mK**2*Q**2*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_pipi_bse(Q)*bubble_loop(Q, mPI)**2*
           log((2.*mK**2 - s + sqrt(s*(-4.*mK**2 + s)))/(2.*mK**2))**2 -
          216.*mPI**2*Q**2*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mK)*log((2.*mPI**2 - s + sqrt(s*(-4.*mPI**2 + s)))/
              (2.*mPI**2))**2 + 216.*mPI**2*Q**2*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_kk_to_kk_bse(Q)*bubble_loop(Q, mK)**2*
           log((2.*mPI**2 - s + sqrt(s*(-4.*mPI**2 + s)))/(2.*mPI**2))**2 +
          216.*mPI**2*(mPI**2 - 2.*Q**2)*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mPI)*log((2.*mPI**2 - s + sqrt(s*(-4.*mPI**2 + s)))/
              (2.*mPI**2))**2 - 144.*sqrt(3.)*mPI**2*(mPI**2 - 2.*Q**2)*
           (mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)*
           log((2.*mPI**2 - s + sqrt(s*(-4.*mPI**2 + s)))/(2.*mPI**2))**2 +
          108.*sqrt(3.)*mPI**2*Q**2*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mK)*bubble_loop(Q, mPI)*
           log((2.*mPI**2 - s + sqrt(s*(-4.*mPI**2 + s)))/(2.*mPI**2))**2 -
          216.*mPI**2*(mPI**2 - 2.*Q**2)*(mPI**2 + Q**2 - s - t)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_pipi_to_pipi_bse(Q)*bubble_loop(Q, mPI)**2*
           log((2.*mPI**2 - s + sqrt(s*(-4.*mPI**2 + s)))/(2.*mPI**2))**2)) / \
      (sqrt(2.)*fpi**4*(ms - Q)*(ms + Q)*(Q**2 - s)**2*vh*
        (3.*vh + 3.*gsff*vs + 2.*gsGG*vs)*(9.*vh + 4.*gsGG*vs))


def __xx_s_pipig_rho_4_bub_E(Q, s, t, params):
    gsxx = params.gsxx
    gsGG = params.gsGG
    gsff = params.gsff
    mx = params.mx
    ms = params.ms
    vs = params.vs

    return (complex(0., 0.0030864197530864196)*gsxx*gv*sqrt(-4.*mx**2 + Q**2)*qe*s*
        (mPI**2 + Q**2 - s - t)*(6.*(fv + 2.*gv)*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_kk_to_kk_bse(Q)*bubble_loop(Q, mK)**2 +
          3.*(3.*fv + 8.*gv)*(9.*gsff*
              (18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mPI)*(-1. +
             amp_pipi_to_pipi_bse(Q)*bubble_loop(Q, mPI)) +
          bubble_loop(Q, mK)*(2.*sqrt(3.)*(3.*fv + 8.*gv)*
              (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
                2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                   mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
              amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mPI) -
             3.*(fv + 2.*gv)*(2.*(9.*gsff*
                    (18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
                   2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                      mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2))) -
                sqrt(3.)*(9.*gsff*(18.*gsGG*Q**2*vh*vs +
                      mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
                   2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                      mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
                 amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mPI)))))/ \
      (sqrt(2.)*fpi**4*mrhoT**2*(ms - Q)*(ms + Q)*
        (mrho**2 - complex(0., 1.)*mrho*rhowidth - s)*vh*(3.*vh + 3.*gsff*vs + 2.*gsGG*vs)*
        (9.*vh + 4.*gsGG*vs))


def __xx_s_pipig_rho_no_bub_E(Q, s, t, params):
    gsxx = params.gsxx
    gsGG = params.gsGG
    gsff = params.gsff
    mx = params.mx
    ms = params.ms
    vs = params.vs

    return (complex(0., 0.037037037037037035)*sqrt(2.)*gsxx*gv*sqrt(-4.*mx**2 + Q**2)*qe*s*
        (mPI**2 + Q**2 - s - t)*((3.*fpi**2*fv*gsGG)/
           (mrho**2 - complex(0., 1.)*mrho*rhowidth - s) -
          (16.*gv*pi**4*s**2*(9.*gsff*
                (18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
               2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                  mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
             bubble_loop(Q, mK))/
           ((Q**2 - s)**2*(-mrho**2 + complex(0., 1.)*mrho*rhowidth + s)*
             (3.*vh + 3.*gsff*vs + 2.*gsGG*vs)*(9.*vh + 4.*gsGG*vs)) -
          (32.*gv*pi**4*s**2*(9.*gsff*
                (18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
               2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                  mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
             bubble_loop(Q, mPI))/
           ((Q**2 - s)**2*(-mrho**2 + complex(0., 1.)*mrho*rhowidth + s)*
             (3.*vh + 3.*gsff*vs + 2.*gsGG*vs)*(9.*vh + 4.*gsGG*vs)) +
          (16.*gv*pi**4*s**2*(9.*gsff*
                (18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
               2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                  mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
             bubble_loop(sqrt(s), mK))/
           ((Q**2 - s)**2*(-mrho**2 + complex(0., 1.)*mrho*rhowidth + s)*
             (3.*vh + 3.*gsff*vs + 2.*gsGG*vs)*(9.*vh + 4.*gsGG*vs)) +
          (32.*gv*pi**4*s**2*(9.*gsff*
                (18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
               2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                  mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
             bubble_loop(sqrt(s), mPI))/
           ((Q**2 - s)**2*(-mrho**2 + complex(0., 1.)*mrho*rhowidth + s)*
             (3.*vh + 3.*gsff*vs + 2.*gsGG*vs)*(9.*vh + 4.*gsGG*vs)) +
          (gv*mK**2*pi**2*s*(9.*gsff*
                (18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
               2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                  mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
             log((2.*mK**2 + Q*(-Q + sqrt(-4.*mK**2 + Q**2)))/(2.*mK**2))**2)/
           ((Q**2 - s)**2*(-mrho**2 + complex(0., 1.)*mrho*rhowidth + s)*
             (3.*vh + 3.*gsff*vs + 2.*gsGG*vs)*(9.*vh + 4.*gsGG*vs)) +
          (2.*gv*mPI**2*pi**2*s*(9.*gsff*
                (18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
               2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                  mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
             log((2.*mPI**2 + Q*(-Q + sqrt(-4.*mPI**2 + Q**2)))/(2.*mPI**2))**2)/
           ((Q**2 - s)**2*(-mrho**2 + complex(0., 1.)*mrho*rhowidth + s)*
             (3.*vh + 3.*gsff*vs + 2.*gsGG*vs)*(9.*vh + 4.*gsGG*vs)) -
          (gv*mK**2*pi**2*s*(9.*gsff*
                (18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
               2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                  mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
             log((2.*mK**2 - s + sqrt(s*(-4.*mK**2 + s)))/(2.*mK**2))**2)/
           ((Q**2 - s)**2*(-mrho**2 + complex(0., 1.)*mrho*rhowidth + s)*
             (3.*vh + 3.*gsff*vs + 2.*gsGG*vs)*(9.*vh + 4.*gsGG*vs)) -
          (2.*gv*mPI**2*pi**2*s*(9.*gsff*
                (18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
               2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                  mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
             log((2.*mPI**2 - s + sqrt(s*(-4.*mPI**2 + s)))/(2.*mPI**2))**2)/
           ((Q**2 - s)**2*(-mrho**2 + complex(0., 1.)*mrho*rhowidth + s)*
             (3.*vh + 3.*gsff*vs + 2.*gsGG*vs)*(9.*vh + 4.*gsGG*vs))))/ \
      (fpi**4*mrhoT**2*(ms - Q)*(ms + Q)*vh)


def __xx_s_pipig_rho_triangle_bub_E(Q, s, t, params):
    gsxx = params.gsxx
    gsGG = params.gsGG
    gsff = params.gsff
    mx = params.mx
    ms = params.ms
    vs = params.vs

    return (complex(0., 0.0030864197530864196)*gsxx*gv**2*pi**2*sqrt(-4.*mx**2 + Q**2)*qe*s**2*
        (mPI**2 + Q**2 - s - t)*(288.*pi**2*Q**2*s*
           (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           amp_kk_to_kk_bse(Q)*bubble_loop(Q, mK)**3 -
          3.*(9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
             2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
           bubble_loop(Q, mPI)*(-1. +
             amp_pipi_to_pipi_bse(Q)*bubble_loop(Q, mPI))*
           (128.*pi**2*(mPI**2 - 2.*Q**2)*s*bubble_loop(Q, mPI) +
             48.*pi**2*Q**2*s*bubble_loop(sqrt(s), mK) -
             128.*mPI**2*pi**2*s*bubble_loop(sqrt(s), mPI) +
             256.*pi**2*Q**2*s*bubble_loop(sqrt(s), mPI) +
             3.*mK**2*Q**2*log((2.*mK**2 + Q*(-Q + sqrt(-4.*mK**2 + Q**2)))/
                 (2.*mK**2))**2 - 8.*mPI**4*
              log((2.*mPI**2 + Q*(-Q + sqrt(-4.*mPI**2 + Q**2)))/(2.*mPI**2))**2 \
    + 16.*mPI**2*Q**2*log((2.*mPI**2 + Q*(-Q + sqrt(-4.*mPI**2 + Q**2)))/
                 (2.*mPI**2))**2 -
             3.*mK**2*Q**2*log((2.*mK**2 - s + sqrt(s*(-4.*mK**2 + s)))/
                 (2.*mK**2))**2 + 8.*mPI**4*
              log((2.*mPI**2 - s + sqrt(s*(-4.*mPI**2 + s)))/(2.*mPI**2))**2 -
             16.*mPI**2*Q**2*log((2.*mPI**2 - s + sqrt(s*(-4.*mPI**2 + s)))/
                 (2.*mPI**2))**2) +
          6.*Q**2*bubble_loop(Q, mK)**2*
           (8.*pi**2*s*(2.*sqrt(3.)*(9.*gsff*
                    (18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
                   2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                      mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
                 amp_pipi_to_kk_bse(Q)*bubble_loop(Q, mPI) +
                3.*(-2.*(9.*gsff*(18.*gsGG*Q**2*vh*vs +
                         mK**2*(9.*vh + 8.*gsGG*vs)**2) +
                      2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                         mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)\
    )) + sqrt(3.)*(9.*gsff*(18.*gsGG*Q**2*vh*vs +
                         mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
                      2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                         mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs -
                            64.*gsGG**2*vs**2)))*amp_pipi_to_kk_bse(Q)*
                    bubble_loop(Q, mPI))) +
             (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
                2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                   mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
              amp_kk_to_kk_bse(Q)*
              (64.*pi**2*s*bubble_loop(Q, mPI) -
                48.*pi**2*s*bubble_loop(sqrt(s), mK) -
                64.*pi**2*s*bubble_loop(sqrt(s), mPI) -
                3.*mK**2*log((2.*mK**2 + Q*(-Q + sqrt(-4.*mK**2 + Q**2)))/
                    (2.*mK**2))**2 -
                4.*mPI**2*log((2.*mPI**2 + Q*(-Q + sqrt(-4.*mPI**2 + Q**2)))/
                    (2.*mPI**2))**2 +
                3.*mK**2*log((2.*mK**2 - s + sqrt(s*(-4.*mK**2 + s)))/
                    (2.*mK**2))**2 +
                4.*mPI**2*log((2.*mPI**2 - s + sqrt(s*(-4.*mPI**2 + s)))/
                    (2.*mPI**2))**2)) +
          bubble_loop(Q, mK)*(-16.*pi**2*s*
              (16.*sqrt(3.)*(mPI**2 - 2.*Q**2)*
                 (9.*gsff*(18.*gsGG*Q**2*vh*vs +
                      mK**2*(9.*vh + 8.*gsGG*vs)**2) +
                   2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                      mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
                 amp_pipi_to_kk_bse(Q) -
                3.*Q**2*(9.*gsff*(18.*gsGG*Q**2*vh*vs +
                      mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
                   2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                      mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
                 (4.*sqrt(3.)*amp_pipi_to_kk_bse(Q) +
                   3.*amp_pipi_to_pipi_bse(Q)))*bubble_loop(Q, mPI)**2 +
             6.*Q**2*(9.*gsff*(18.*gsGG*Q**2*vh*vs +
                   mK**2*(9.*vh + 8.*gsGG*vs)**2) +
                2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                   mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
              (48.*pi**2*s*bubble_loop(sqrt(s), mK) +
                64.*pi**2*s*bubble_loop(sqrt(s), mPI) +
                3.*mK**2*log((2.*mK**2 + Q*(-Q + sqrt(-4.*mK**2 + Q**2)))/
                    (2.*mK**2))**2 +
                4.*mPI**2*log((2.*mPI**2 + Q*(-Q + sqrt(-4.*mPI**2 + Q**2)))/
                    (2.*mPI**2))**2 -
                3.*mK**2*log((2.*mK**2 - s + sqrt(s*(-4.*mK**2 + s)))/
                    (2.*mK**2))**2 -
                4.*mPI**2*log((2.*mPI**2 - s + sqrt(s*(-4.*mPI**2 + s)))/
                    (2.*mPI**2))**2) -
             bubble_loop(Q, mPI)*(2.*sqrt(3.)*
                 (9.*gsff*(18.*gsGG*Q**2*vh*vs + mK**2*(9.*vh + 8.*gsGG*vs)**2) +
                   2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                      mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2)))*
                 amp_pipi_to_kk_bse(Q)*
                 (48.*pi**2*Q**2*s*bubble_loop(sqrt(s), mK) -
                   128.*pi**2*(mPI**2 - 2.*Q**2)*s*bubble_loop(sqrt(s), mPI) +
                   3.*mK**2*Q**2*log((2.*mK**2 +
                         Q*(-Q + sqrt(-4.*mK**2 + Q**2)))/(2.*mK**2))**2 -
                   8.*mPI**4*log((2.*mPI**2 + Q*(-Q + sqrt(-4.*mPI**2 + Q**2)))/
                       (2.*mPI**2))**2 +
                   16.*mPI**2*Q**2*
                    log((2.*mPI**2 + Q*(-Q + sqrt(-4.*mPI**2 + Q**2)))/
                       (2.*mPI**2))**2 -
                   3.*mK**2*Q**2*log((2.*mK**2 - s + sqrt(s*(-4.*mK**2 + s)))/
                       (2.*mK**2))**2 +
                   8.*mPI**4*log((2.*mPI**2 - s + sqrt(s*(-4.*mPI**2 + s)))/
                       (2.*mPI**2))**2 -
                   16.*mPI**2*Q**2*log((2.*mPI**2 - s +
                         sqrt(s*(-4.*mPI**2 + s)))/(2.*mPI**2))**2) +
                3.*Q**2*(16.*pi**2*s*
                    (9.*gsff*(8.*mK**2*(9.*vh + 8.*gsGG*vs)**2 +
                         3.*(66.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2)\
    ) - 2.*gsGG*(-8.*mK**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2) +
                         3.*(-99.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                            mPI**2*
                             (-81.*vh**2 + 144.*gsGG*vh*vs + 64.*gsGG**2*vs**2)))) \
    + sqrt(3.)*(9.*gsff*(18.*gsGG*Q**2*vh*vs + mPI**2*(9.*vh + 8.*gsGG*vs)**2) +
                      2.*gsGG*(27.*Q**2*vh*(3.*vh + 2.*gsGG*vs) +
                         mPI**2*(81.*vh**2 - 144.*gsGG*vh*vs - 64.*gsGG**2*vs**2))\
    )*amp_pipi_to_kk_bse(Q)*
                    (48.*pi**2*s*bubble_loop(sqrt(s), mK) +
                      64.*pi**2*s*bubble_loop(sqrt(s), mPI) +
                      3.*mK**2*log((2.*mK**2 + Q*(-Q + sqrt(-4.*mK**2 + Q**2)))/
                          (2.*mK**2))**2 +
                      4.*mPI**2*log((2.*mPI**2 +
                            Q*(-Q + sqrt(-4.*mPI**2 + Q**2)))/(2.*mPI**2))**2 -
                      3.*mK**2*log((2.*mK**2 - s + sqrt(s*(-4.*mK**2 + s)))/
                          (2.*mK**2))**2 -
                      4.*mPI**2*log((2.*mPI**2 - s + sqrt(s*(-4.*mPI**2 + s)))/
                          (2.*mPI**2))**2))))))/ \
      (sqrt(2.)*fpi**6*mrhoT**2*(ms - Q)*(ms + Q)*(Q**2 - s)**2*
        (-mrho**2 + complex(0., 1.)*mrho*rhowidth + s)*vh*(3.*vh + 3.*gsff*vs + 2.*gsGG*vs)*
        (9.*vh + 4.*gsGG*vs))


def __xx_s_pipig_E(Q, s, t, params):
    return __xx_s_pipig_no_rho_5_bub_E(Q, s, t, params) + \
            __xx_s_pipig_no_rho_fsr_bub_E(Q, s, t, params) + \
            __xx_s_pipig_no_rho_no_bub_E(Q, s, t, params) + \
            __xx_s_pipig_no_rho_triangle_bub_E(Q, s, t, params) + \
            __xx_s_pipig_rho_4_bub_E(Q, s, t, params) + \
            __xx_s_pipig_rho_no_bub_E(Q, s, t, params) + \
            __xx_s_pipig_rho_triangle_bub_E(Q, s, t, params)


def msqrd_xx_s_pipig(Q, s, t, params):
    """Compute matrix element squared for xbar x -> s^* -> pi+ pi- g.

    Notes
    -----
    The matrix element for this process, M, is related to the form factor by
        |M|^2. = s Re[E(s,t,u) E^*(s,u,t)] - m_PI^2. |E(s,t,u) + E(s,u,t)|^2.
    """
    u = Q**2 + 2. * mPI**2 - s - t

    E_t = __xx_s_pipig_E(Q, s, t, params)
    E_u = __xx_s_pipig_E(Q, s, u, params)

    return s * (E_t * E_u.conjugate()).real - mPI**2 * abs(E_t + E_u)**2
