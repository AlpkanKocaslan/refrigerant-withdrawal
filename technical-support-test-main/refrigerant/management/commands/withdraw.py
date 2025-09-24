from django.core.management.base import BaseCommand
from django.db.models import F
from ...models import Vessel
import threading



class Command(BaseCommand):
    help = "Simulate condition when withdrawing refrigerant from a vessel."

    def handle(self, *args, **kwargs):
        Vessel.objects.create(name="Test Vessel", content=50.0)
        self.stdout.write("Simulating condition...")
        self.run_simulation()

    def run_simulation(self):
        barrier = threading.Barrier(2)

        def user1():
            withdraw_amount = 10.0 
            barrier.wait()
            updated = Vessel.objects.filter(id=1, content__gte=withdraw_amount).update(content=F('content') - withdraw_amount)
            if not updated:
                self.stdout.write("Vessel is empty, withdrawal not possible.")

        def user2():
            withdraw_amount = 10.0 
            barrier.wait()
            updated = Vessel.objects.filter(id=1, content__gte=withdraw_amount).update(content=F('content') - withdraw_amount)
            if not updated:
                self.stdout.write("Vessel is empty, withdrawal not possible.")

        t1 = threading.Thread(target=user1)
        t2 = threading.Thread(target=user2)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        vessel = Vessel.objects.get(id=1)
        self.stdout.write(f"Remaining content: {vessel.content} kg")
