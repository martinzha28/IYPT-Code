public class SaxonBowl {
    
    public static double dischargeCoefficient(double deltaP)
    {        
        double a = -0.0000143;
        double b = 0.0071369;
        double c = -0.329;
        
        return (a*deltaP*deltaP) + (b*deltaP) + (c);
}

    public static void main(String[] args) {
//        double r = 15.0 / 1000; // replace
        double mB = 285.3 / 1000; // for varying diameter
//        double mB = 350.0/1000;
        double mb = mB;
//        double h0 = 150.0/1000;
//        double h0 = 20.0/1000;
        
        while (mb == mB) {
            // universal constants
            double rho = 998;
            double pi = Math.PI;
            double g = 9.81;
//            double r = 6.3/2000;
            double r = 2.65/1000;
            double h0 = 100.67/1000;
            

            // system constants
            double R = 123.06/2000; // 120.0 / 2000, 51.66/2000
            double T = 1.11 / 1000; // 2.0/1000
            double TPlate = 12.0 / 1000; // 12.0/1000

            double cd = 0.74; // 0.74
            double xb = 0.005; // replace later

            // method constants
            double t = 0;
            double totalTime = 10;
            double dt = 0.0002;

            // system variables
            double xl = 0.0;
            double xlVel = 0.0;
            double h = 0.0;
            double hVel = 0.0;
            double xw = TPlate + (h / 2);
            double xwVel = 0.0;
            double mw = 0.0;
            double mwDot = 0.0;
            double xc = ((mb * xl) - (mb * xb) + (mw * xl) - (mw * xw)) / (mb + mw);
            double xcVel = 0.0;
            double xcAcc;
            double mc = mb + mw;
            double mcDot = mwDot;
            double cf = 0.82;
            double mu = 0.9775*Math.pow(10,-3);
            
            double gamma = 72.28/100000;
	  double surfaceAngle = 67.7;
            double perimeter = 2*pi*R*100;
 while (xl < h0+TPlate) {
                xcAcc = (g * (1 - ((rho * pi * R * R * xl) / mc))) - ((mcDot / mc) * xcVel) - (gamma*perimeter*Math.cos((surfaceAngle/180)*pi)/mc) - (0.5*rho*pi*R*R*cf*xlVel*xlVel*Math.signum(xlVel)/mc) - (1.328*pi*R*Math.sqrt(rho*mu*Math.pow(Math.abs(xlVel), 3)*Math.abs(xl))*Math.signum(xlVel)/mc);
                xcVel = xcVel + (xcAcc * dt);
                xc = xc + (xcVel * dt) + (0.5*xcAcc*dt*dt);
                xl = ((xc * (mb + mw)) + (mb * xb) + (mw * xw)) / (mb + mw);
                xlVel = xcVel + ((mwDot * ((mb * xl) - (mb * xb) + (mw * xl) - (mw * xw))) / (Math.pow(mb + mw, 2))) + (((mwDot * xw) - (mwDot * xl) + (mw * xwVel)) / (mb + mw));
                hVel = dischargeCoefficient(rho*g*(xl-h)) * Math.sqrt(2.0 * g * (xl - h)) * Math.pow(r / R, 2);
                h = h + (hVel * dt);
                xw = TPlate + (h / 2);
                xwVel = 0.5 * hVel;

                mw = rho * pi * Math.pow(R - T, 2) * h;
                mwDot = rho * pi * Math.pow(R - T, 2) * hVel;

                mc = mb + mw;
                mcDot = mwDot;
                
                if (t % 0.05 < dt) {
//                    System.out.println(t + "\t" + -xl);
//                    System.out.println(rho*Math.pow(R/r,2)*hVel*r*2/mu);
                }               
                t = t + dt;
            }          
            System.out.println(dt + "\t" + t);
            
//            r = r-0.0001;
            mb = mb - 0.01;
//            h0 = h0 - (1.0/1000);
//            mb = mb - 100;
        }
    }
}
